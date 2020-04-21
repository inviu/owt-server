# A cmake file for compile fdk-aac
# Author: kaychan
# Mail: 1203375695@qq.com
#
# fdk-aac download: http://www.linuxfromscratch.org/blfs/view/svn/multimedia/fdk-aac.html
# fdk-aac version: fdk-aac-2.0.1
# cmake version: cmake-3.16.0-rc4-win64-x64
 
# Disable in-source builds to prevent source tree corruption.
if(" ${CMAKE_SOURCE_DIR}" STREQUAL " ${CMAKE_BINARY_DIR}")
  message(FATAL_ERROR "
FATAL: In-source builds are not allowed.
       You should create a separate directory for build files.
")
endif()
 
cmake_minimum_required ( VERSION 3.0 )
 
# 声明工程
project ( fdk-aac )
 
set ( SOURCE_FILES )
 
# 遍历添加源码文件
foreach ( subdir
    libAACdec libAACenc libArithCoding 
	libDRCdec 
	libFDK 
    libMpegTPDec libMpegTPEnc
    libPCMutils
	libSACdec libSACenc libSBRdec libSBRenc libSYS)
 
    set ( incdir ${CMAKE_SOURCE_DIR}/${subdir}/include )
	set ( srcdir ${CMAKE_SOURCE_DIR}/${subdir}/src )
	
	# 指定包含目录
    include_directories ( ${incdir} )
	
	# 安装include头文件
    install ( DIRECTORY ${incdir}/ DESTINATION ${CMAKE_INSTALL_PREFIX}/include )
 
    file ( GLOB srcfiles
        ${srcdir}/*.cpp
        ${srcdir}/*.h )
    list ( APPEND SOURCE_FILES ${srcfiles} )
endforeach ()
 
# 编译/安装静态库
add_library ( fdk-aac STATIC ${SOURCE_FILES} )
install ( TARGETS fdk-aac ARCHIVE DESTINATION ${CMAKE_INSTALL_PREFIX}/lib )
 
# 编译/安装动态库
# add_library ( fdk-aac SHARED ${SOURCE_FILES} )
# install ( TARGETS fdk-aac LIBRARY DESTINATION ${CMAKE_INSTALL_PREFIX}/lib )
