{
  'targets': [{
    'target_name': 'videoAnalyzer-sw',
    'sources': [
      '../addon.cc',
      '../VideoTranscoderWrapper.cpp',
      '../VideoTranscoder.cpp',
      '../../../../core/owt_base/MediaFramePipeline.cpp',
      '../../../../core/owt_base/FrameConverter.cpp',
      '../../../../core/owt_base/FrameAnalyzer.cpp',
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
        '-DBUILD_FOR_ANALYTICS',
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
                      '$(CORE_HOME)/../../build/libdeps/ffmpeg-4.1.3',
                      '$(CORE_HOME)/../../third_party/boost_1.72.0/include',
					            '$(CORE_HOME)/../../third_party/log4cxx/src/apache-log4cxx-0.10.0/src/main/include',
    ],
    'library_dirs': [
      '$(CORE_HOME)/../../build/libdeps/build/lib',
      '$(CORE_HOME)/../../third_party/boost_1.72.0/lib/windows/x64/release',
      '$(CORE_HOME)/../../third_party/lib',
    ],    
    'libraries': [
      '-lboost_thread-vc140-mt.lib',
      '-llog4cxx',
      '-lwebrtc',
      '-lavutil',
      '-lavcodec',
      '-lavformat',
      '-lavfilter',
      '-lSvtHevcEnc',
      '-lopenh264',
      '-lwinmm.lib',
    ],
  }]
}
