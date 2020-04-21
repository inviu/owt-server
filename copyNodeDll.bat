set targentAgent=audio_agent
set rootdir=%~dp0
xcopy ..\source\agent\audio\audioMixer\build\Release\audioMixer.node ..\dist\%targentAgent%\audioMixer\build\Release /Y
xcopy %rootdir%source\agent\addons\internalIO\build\Release\internalIO.node %rootdir%dist\%targentAgent%\internalIO\build\Release /Y
xcopy %rootdir%source\agent\addons\logger\build\Release\logger.node %rootdir%dist\%targentAgent%\logger\build\Release /Y
xcopy %rootdir%source\agent\addons\mediaFrameMulticaster\build\Release\mediaFrameMulticaster.node %rootdir%dist\%targentAgent%\mediaFrameMulticaster\build\Release /Y
xcopy %rootdir%third_party\lib\log4cxx.dll %rootdir%dist\%targentAgent%\ /Y
xcopy %rootdir%build\libdeps\build\bin\avcodec-58.dll %rootdir%dist\%targentAgent%\ /Y
xcopy %rootdir%build\libdeps\build\bin\avdevice-58.dll %rootdir%dist\%targentAgent%\ /Y
xcopy %rootdir%build\libdeps\build\bin\avfilter-7.dll %rootdir%dist\%targentAgent%\ /Y
xcopy %rootdir%build\libdeps\build\bin\avformat-58.dll %rootdir%dist\%targentAgent%\ /Y
xcopy %rootdir%build\libdeps\build\bin\avutil-56.dll %rootdir%dist\%targentAgent%\ /Y
xcopy %rootdir%build\libdeps\build\bin\swresample-3.dll %rootdir%dist\%targentAgent%\ /Y
xcopy %rootdir%build\libdeps\build\bin\swscale-5.dll %rootdir%dist\%targentAgent%\ /Y


set targentAgent=recording_agent
xcopy %rootdir%source\agent\addons\avstreamLib\build\Release\avstream.node %rootdir%dist\%targentAgent%\avstreamLib\build\Release /Y
xcopy %rootdir%source\agent\addons\internalIO\build\Release\internalIO.node %rootdir%dist\%targentAgent%\internalIO\build\Release /Y
xcopy %rootdir%source\agent\addons\logger\build\Release\logger.node %rootdir%dist\%targentAgent%\logger\build\Release /Y
xcopy %rootdir%third_party\lib\log4cxx.dll %rootdir%dist\%targentAgent%\ /Y
xcopy %rootdir%third_party\lib\SvtHevcEnc.dll %rootdir%dist\%targentAgent%\ /Y
xcopy %rootdir%third_party\lib\openh264.dll %rootdir%dist\%targentAgent%\ /Y
xcopy %rootdir%build\libdeps\build\bin\avcodec-58.dll %rootdir%dist\%targentAgent%\ /Y
xcopy %rootdir%build\libdeps\build\bin\avdevice-58.dll %rootdir%dist\%targentAgent%\ /Y
xcopy %rootdir%build\libdeps\build\bin\avfilter-7.dll %rootdir%dist\%targentAgent%\ /Y
xcopy %rootdir%build\libdeps\build\bin\avformat-58.dll %rootdir%dist\%targentAgent%\ /Y
xcopy %rootdir%build\libdeps\build\bin\avutil-56.dll %rootdir%dist\%targentAgent%\ /Y
xcopy %rootdir%build\libdeps\build\bin\swresample-3.dll %rootdir%dist\%targentAgent%\ /Y
xcopy %rootdir%build\libdeps\build\bin\swscale-5.dll %rootdir%dist\%targentAgent%\ /Y


set targentAgent=streaming_agent
xcopy %rootdir%source\agent\addons\avstreamLib\build\Release\avstream.node %rootdir%dist\%targentAgent%\avstreamLib\build\Release /Y
xcopy %rootdir%source\agent\addons\internalIO\build\Release\internalIO.node %rootdir%dist\%targentAgent%\internalIO\build\Release /Y
xcopy %rootdir%source\agent\addons\logger\build\Release\logger.node %rootdir%dist\%targentAgent%\logger\build\Release /Y
xcopy %rootdir%third_party\lib\log4cxx.dll %rootdir%dist\%targentAgent%\ /Y
xcopy %rootdir%third_party\lib\SvtHevcEnc.dll %rootdir%dist\%targentAgent%\ /Y
xcopy %rootdir%third_party\lib\openh264.dll %rootdir%dist\%targentAgent%\ /Y
xcopy %rootdir%build\libdeps\build\bin\avcodec-58.dll %rootdir%dist\%targentAgent%\ /Y
xcopy %rootdir%build\libdeps\build\bin\avdevice-58.dll %rootdir%dist\%targentAgent%\ /Y
xcopy %rootdir%build\libdeps\build\bin\avfilter-7.dll %rootdir%dist\%targentAgent%\ /Y
xcopy %rootdir%build\libdeps\build\bin\avformat-58.dll %rootdir%dist\%targentAgent%\ /Y
xcopy %rootdir%build\libdeps\build\bin\avutil-56.dll %rootdir%dist\%targentAgent%\ /Y
xcopy %rootdir%build\libdeps\build\bin\swresample-3.dll %rootdir%dist\%targentAgent%\ /Y
xcopy %rootdir%build\libdeps\build\bin\swscale-5.dll %rootdir%dist\%targentAgent%\ /Y


set targentAgent=video_agent
xcopy %rootdir%source\agent\addons\internalIO\build\Release\internalIO.node %rootdir%dist\%targentAgent%\internalIO\build\Release /Y
xcopy %rootdir%source\agent\addons\logger\build\Release\logger.node %rootdir%dist\%targentAgent%\logger\build\Release /Y
xcopy %rootdir%source\agent\addons\mediaFrameMulticaster\build\Release\mediaFrameMulticaster.node %rootdir%dist\%targentAgent%\mediaFrameMulticaster\build\Release /Y
xcopy %rootdir%source\agent\video\videoMixer\videoMixer_sw\build\Release\videoMixer-sw.node %rootdir%dist\%targentAgent%\videoMixer_sw\build\Release /Y
xcopy %rootdir%source\agent\video\videoTranscoder\videoTranscoder_sw\build\Release\videoTranscoder-sw.node %rootdir%dist\%targentAgent%\videoTranscoder_sw\build\Release /Y
xcopy %rootdir%third_party\lib\log4cxx.dll %rootdir%dist\%targentAgent%\ /Y
xcopy %rootdir%third_party\lib\SvtHevcEnc.dll %rootdir%dist\%targentAgent%\ /Y
xcopy %rootdir%third_party\lib\openh264.dll %rootdir%dist\%targentAgent%\ /Y
xcopy %rootdir%build\libdeps\build\bin\avcodec-58.dll %rootdir%dist\%targentAgent%\ /Y
xcopy %rootdir%build\libdeps\build\bin\avdevice-58.dll %rootdir%dist\%targentAgent%\ /Y
xcopy %rootdir%build\libdeps\build\bin\avfilter-7.dll %rootdir%dist\%targentAgent%\ /Y
xcopy %rootdir%build\libdeps\build\bin\avformat-58.dll %rootdir%dist\%targentAgent%\ /Y
xcopy %rootdir%build\libdeps\build\bin\avutil-56.dll %rootdir%dist\%targentAgent%\ /Y
xcopy %rootdir%build\libdeps\build\bin\swresample-3.dll %rootdir%dist\%targentAgent%\ /Y
xcopy %rootdir%build\libdeps\build\bin\swscale-5.dll %rootdir%dist\%targentAgent%\ /Y


set targentAgent=webrtc_agent
xcopy %rootdir%source\agent\addons\internalIO\build\Release\internalIO.node %rootdir%dist\%targentAgent%\internalIO\build\Release /Y
xcopy %rootdir%source\agent\addons\logger\build\Release\logger.node %rootdir%dist\%targentAgent%\logger\build\Release /Y
xcopy %rootdir%source\agent\webrtc\webrtcLib\build\Release\webrtc.node %rootdir%dist\%targentAgent%\webrtcLib\build\Release /Y
xcopy %rootdir%third_party\lib\log4cxx.dll %rootdir%dist\%targentAgent%\ /Y
xcopy %rootdir%build\libdeps\build\bin\libeay32.dll %rootdir%dist\%targentAgent%\ /Y
xcopy %rootdir%build\libdeps\build\bin\ssleay32.dll %rootdir%dist\%targentAgent%\ /Y
xcopy %rootdir%build\libdeps\build\bin\libnice.dll %rootdir%dist\%targentAgent%\ /Y
xcopy %rootdir%build\libdeps\build\bin\avutil-56.dll %rootdir%dist\%targentAgent%\ /Y
xcopy %rootdir%build\libdeps\build\bin\avcodec-58.dll %rootdir%dist\%targentAgent%\ /Y
xcopy %rootdir%build\libdeps\build\bin\avformat-58.dll %rootdir%dist\%targentAgent%\ /Y
xcopy %rootdir%build\libdeps\build\bin\swresample-3.dll %rootdir%dist\%targentAgent%\ /Y
xcopy %rootdir%build\libdeps\glib\bin\libz-1.dll %rootdir%dist\%targentAgent%\ /Y
xcopy %rootdir%build\libdeps\glib\bin\libwinpthread-1.dll %rootdir%dist\%targentAgent%\ /Y
xcopy %rootdir%build\libdeps\glib\bin\libtasn1-6.dll %rootdir%dist\%targentAgent%\ /Y
xcopy %rootdir%build\libdeps\glib\bin\libnettle-6.dll %rootdir%dist\%targentAgent%\ /Y
xcopy %rootdir%build\libdeps\glib\bin\libintl-8.dll %rootdir%dist\%targentAgent%\ /Y
xcopy %rootdir%build\libdeps\glib\bin\libhogweed-4.dll %rootdir%dist\%targentAgent%\ /Y
xcopy %rootdir%build\libdeps\glib\bin\libgobject-2.0-0.dll %rootdir%dist\%targentAgent%\ /Y
xcopy %rootdir%build\libdeps\glib\bin\libgnutls-30.dll %rootdir%dist\%targentAgent%\ /Y
xcopy %rootdir%build\libdeps\glib\bin\libgmp-10.dll %rootdir%dist\%targentAgent%\ /Y
xcopy %rootdir%build\libdeps\glib\bin\libgmodule-2.0-0.dll %rootdir%dist\%targentAgent%\ /Y
xcopy %rootdir%build\libdeps\glib\bin\libglib-2.0-0.dll %rootdir%dist\%targentAgent%\ /Y
xcopy %rootdir%build\libdeps\glib\bin\libgio-2.0-0.dll %rootdir%dist\%targentAgent%\ /Y
xcopy %rootdir%build\libdeps\glib\bin\libffi-7.dll %rootdir%dist\%targentAgent%\ /Y
