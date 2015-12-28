/*
 * Copyright 2015 Intel Corporation All Rights Reserved. 
 * 
 * The source code contained or described herein and all documents related to the 
 * source code ("Material") are owned by Intel Corporation or its suppliers or 
 * licensors. Title to the Material remains with Intel Corporation or its suppliers 
 * and licensors. The Material contains trade secrets and proprietary and 
 * confidential information of Intel or its suppliers and licensors. The Material 
 * is protected by worldwide copyright and trade secret laws and treaty provisions. 
 * No part of the Material may be used, copied, reproduced, modified, published, 
 * uploaded, posted, transmitted, distributed, or disclosed in any way without 
 * Intel's prior express written permission.
 * 
 * No license under any patent, copyright, trade secret or other intellectual 
 * property right is granted to or conferred upon you by disclosure or delivery of 
 * the Materials, either expressly, by implication, inducement, estoppel or 
 * otherwise. Any license under such intellectual property rights must be express 
 * and approved by Intel in writing.
 */

#include "InternalOut.h"

namespace woogeen_base {

InternalOut::InternalOut(const std::string& protocol, const std::string& dest_ip, unsigned int dest_port)
{
    Protocol proto = (protocol == "tcp") ? woogeen_base::TCP : woogeen_base::UDP;

    m_transport.reset(new woogeen_base::RawTransport(this, proto));
    m_transport->createConnection(dest_ip, dest_port);
}

InternalOut::~InternalOut()
{
    m_transport->close();
}

void InternalOut::onFrame(const Frame& frame)
{
    char sendBuffer[TRANSPORT_BUFFER_SIZE];
    size_t header_len = sizeof(Frame);
    if (header_len + frame.length + 1 > TRANSPORT_BUFFER_SIZE) {
        //TODO: frame too big, log warn here.
        return;
    }

    sendBuffer[0] = TDT_MEDIA_FRAME;
    memcpy(&sendBuffer[1], reinterpret_cast<char*>(const_cast<Frame*>(&frame)), header_len);
    memcpy(&sendBuffer[1+header_len], reinterpret_cast<char*>(frame.payload), frame.length);
    m_transport->sendData(sendBuffer, header_len + frame.length + 1);
}

void InternalOut::onTransportData(char* buf, int len)
{
    switch (buf[0]) {
        case TDT_FEEDBACK_MSG:
            deliverFeedbackMsg(*(reinterpret_cast<FeedbackMsg*>(buf + 1)));
        default:
            break;
    }
}


} /* namespace woogeen_base */

