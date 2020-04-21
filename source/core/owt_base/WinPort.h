#pragma once

#include <time.h>
#ifdef WIN32
#include <WinSock2.h>
#include <Windows.h>
#else
#include <sys/time.h>
#endif
#ifdef WIN32
int gettimeofday(struct timeval *tp, void *tzp);
#endif
