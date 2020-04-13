// Copyright (C) <2019> Intel Corporation
//
// SPDX-License-Identifier: Apache-2.0

#include <time.h>
#ifdef WIN32
#   include <winsock2.h>
#   include <windows.h>
#else
#   include <sys/time.h>
#endif

#ifdef WIN32
int
gettimeofday(struct timeval *tp, void *tzp)
{
    time_t clock;
    struct tm tm;
    SYSTEMTIME wtm;

    GetLocalTime(&wtm);
    tm.tm_year     = wtm.wYear - 1900;
    tm.tm_mon     = wtm.wMonth - 1;
    tm.tm_mday     = wtm.wDay;
    tm.tm_hour     = wtm.wHour;
    tm.tm_min     = wtm.wMinute;
    tm.tm_sec     = wtm.wSecond;
    tm. tm_isdst    = -1;
    clock = mktime(&tm);
    tp->tv_sec = clock;
    tp->tv_usec = wtm.wMilliseconds * 1000;

    return (0);
}
#endif


#include "AudioTime.h"

namespace mcu {

uint32_t AudioTime::sTimestampOffset = 0;

void AudioTime::setTimestampOffset(uint32_t offset)
{
    sTimestampOffset = offset;
}

int64_t AudioTime::currentTime(void)
{
    timeval time;
    gettimeofday(&time, nullptr);
    return ((time.tv_sec * 1000) + (time.tv_usec / 1000)) - sTimestampOffset;
}

} /* namespace mcu */
