{
  'targets': [{
    'target_name': 'avstream',
    'sources': [
      'addon.cc',
      'AVStreamInWrap.cc',
      'AVStreamOutWrap.cc',
      '../../addons/common/NodeEventRegistry.cc',
      '../../../core/owt_base/MediaFramePipeline.cpp',
      '../../../core/owt_base/AVStreamOut.cpp',
      '../../../core/owt_base/MediaFileOut.cpp',
      '../../../core/owt_base/LiveStreamOut.cpp',
      '../../../core/owt_base/LiveStreamIn.cpp',
      '../../../core/owt_base/WinPort.cpp',
    ],
    'defines': [
            'NOMINMAX',
            '_WIN32_WINNT=0x0A00',
            'WIN32_LEAN_AND_MEAN',
          ],
    "msvs_settings": {
          "VCCLCompilerTool": {
            'RuntimeTypeInfo': 'true',
            "ExceptionHandling": "1",
            'AdditionalOptions': ['/GR','/FI\"winsock2.h\"','/FI\"windows.h\"']
          },
      },
    'include_dirs': [ '$(CORE_HOME)/common',
                      '$(CORE_HOME)/owt_base',
                      '$(CORE_HOME)/../../build/libdeps/build/include',
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
      '-lavutil',
      '-lavcodec',
      '-lavformat',
      '-lswresample',
    ],
    'conditions': [
      [ 'OS=="mac"', {
        'xcode_settings': {
          'GCC_ENABLE_CPP_EXCEPTIONS': 'YES',        # -fno-exceptions
          'MACOSX_DEPLOYMENT_TARGET':  '10.7',       # from MAC OS 10.7
          'OTHER_CFLAGS': ['-g -O$(OPTIMIZATION_LEVEL) -stdlib=libc++']
        },
      }, { # OS!="mac"
        'cflags!':    ['-fno-exceptions'],
        'cflags_cc':  ['-Wall', '-O$(OPTIMIZATION_LEVEL)', '-g', '-std=c++11'],
        'cflags_cc!': ['-fno-exceptions']
      }],
    ]
  }]
}
