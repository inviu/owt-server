{
  'targets': [{
    'target_name': 'videoTranscoder-sw',
    'sources': [
      '../addon.cc',
      '../VideoTranscoderWrapper.cpp',
      '../VideoTranscoder.cpp',
      '../../../../core/owt_base/MediaFramePipeline.cpp',
      '../../../../core/owt_base/FrameConverter.cpp',
      '../../../../core/owt_base/I420BufferManager.cpp',
      '../../../../core/owt_base/VCMFrameDecoder.cpp',
      '../../../../core/owt_base/VCMFrameEncoder.cpp',
      '../../../../core/owt_base/FFmpegFrameDecoder.cpp',
      '../../../../core/owt_base/FrameProcesser.cpp',
      '../../../../core/owt_base/FFmpegDrawText.cpp',
      '../../../../core/owt_base/SVTHEVCEncoder.cpp',
    ],
    'defines': [
            'WEBRTC_WIN',
            'NOMINMAX',
            'ENABLE_SVT_HEVC_ENCODER',
            '_WIN32_WINNT=0x0A00',
          ],
    "msvs_settings": {
          "VCCLCompilerTool": {
            'RuntimeTypeInfo': 'true',
            "ExceptionHandling": "1",
            'AdditionalOptions': ['/GR'], 
            # "DisableSpecificWarnings": [
            #   "4244"
            # ],
          },
          # "VCLinkerTool": {
          #   "LinkTimeCodeGeneration": 1,
          #   "OptimizeReferences": 2,
          #   "EnableCOMDATFolding": 2,
          #   "LinkIncremental": 1,
          # }
      },
    'cflags_cc': [
        '-Wall',
        '-O$(OPTIMIZATION_LEVEL)',
        '-g',
        '-std=c++11',
        '-DWEBRTC_POSIX',
        '-DENABLE_SVT_HEVC_ENCODER',
    ],
    'cflags_cc!': [
        '-fno-exceptions',
    ],
    'include_dirs': [ '..',
                      '$(CORE_HOME)/common',
                      '$(CORE_HOME)/owt_base',
                      '$(CORE_HOME)/../../third_party/webrtc/src',
                      '$(CORE_HOME)/../../third_party/webrtc/src/third_party/libyuv/include',
                      '$(CORE_HOME)/../../build/libdeps/build/include',
                      'D:/workspace/vcpkg/installed/x64-windows-static/include',
					            'D:/workspace/log4cxx/src/apache-log4cxx-0.10.0/src/main/include',
    ],
    'libraries': [
      '-lD:/workspace/vcpkg/installed/x64-windows-static/lib/boost_thread-vc140-mt.lib',
      '-lD:/workspace/log4cxx/src/apache-log4cxx-0.10.0/projects/x64/Release/log4cxx',
      '-l$(CORE_HOME)/../../third_party/webrtc/webrtc',
      '-l$(CORE_HOME)/../../third_party/openh264/openh264',
      '-l$(CORE_HOME)/../../build/libdeps/build/bin/avutil',
      '-l$(CORE_HOME)/../../build/libdeps/build/bin/avcodec',
      '-l$(CORE_HOME)/../../build/libdeps/build/bin/avformat',
      '-l$(CORE_HOME)/../../build/libdeps/build/bin/avfilter',
      '-l$(CORE_HOME)/../../third_party/SVT-HEVC/Bin/Release/SvtHevcEnc',
      '-lwinmm.lib',
    ],
  }]
}
