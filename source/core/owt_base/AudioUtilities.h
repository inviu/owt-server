// Copyright (C) <2019> Intel Corporation
//
// SPDX-License-Identifier: Apache-2.0

#ifndef AudioUtilities_h
#define AudioUtilities_h
#include <time.h>
#ifdef WIN32
#   include <winsock2.h>
#   include <windows.h>
#else
#   include <sys/time.h>
#endif

#ifdef WIN32
int
gettimeofday(struct timeval *tp, void *tzp);
// {
//     time_t clock;
//     struct tm tm;
//     SYSTEMTIME wtm;
//
//     GetLocalTime(&wtm);
//     tm.tm_year     = wtm.wYear - 1900;
//     tm.tm_mon     = wtm.wMonth - 1;
//     tm.tm_mday     = wtm.wDay;
//     tm.tm_hour     = wtm.wHour;
//     tm.tm_min     = wtm.wMinute;
//     tm.tm_sec     = wtm.wSecond;
//     tm. tm_isdst    = -1;
//     clock = mktime(&tm);
//     tp->tv_sec = clock;
//     tp->tv_usec = wtm.wMilliseconds * 1000;
//
//     return (0);
// }
#endif

#include <webrtc/common_types.h>

#include "MediaFramePipeline.h"



namespace owt_base {

static inline int64_t currentTimeMs()
{
    timeval time;
    gettimeofday(&time, nullptr);
    return ((time.tv_sec * 1000) + (time.tv_usec / 1000));
}

FrameFormat getAudioFrameFormat(int pltype);
bool getAudioCodecInst(owt_base::FrameFormat format, webrtc::CodecInst& audioCodec);
int getAudioPltype(owt_base::FrameFormat format);
int32_t getAudioSampleRate(const owt_base::FrameFormat format);
uint32_t getAudioChannels(const owt_base::FrameFormat format);

} /* namespace owt_base */

#endif /* AudioUtilities_h */
