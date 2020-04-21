set rootdir=%~dp0

call "C:\Program Files (x86)\Microsoft Visual Studio\2017\Professional\VC\Auxiliary\Build\vcvarsall.bat" amd64

set MSYS=D:\msys64\usr\bin
PATH=%MSYS%;%path%

set NASM=D:\workspace\vcpkg\downloads\tools\nasm\nasm-2.14.02\nasm.exe
PATH=%NASM%;%path%

set INCLUDE=%INCLUDE%

set LIB=%lib% 
bash -c "make OS=msvc ARCH=x86_64"

xcopy %rootdir%openh264.lib  %rootdir%../lib /Y
xcopy %rootdir%openh264.dll  %rootdir%../lib /Y
pause
