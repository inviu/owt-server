{
  'targets': [{
    'target_name': 'internalIO',
    'sources': [
      'addon.cc',
      'InternalInWrapper.cc',
      'InternalOutWrapper.cc',
      'InternalIOWrapper.cc',
      '../../../core/owt_base/InternalIn.cpp',
      '../../../core/owt_base/InternalOut.cpp',
      '../../../core/owt_base/InternalSctp.cpp',
      '../../../core/owt_base/MediaFramePipeline.cpp',
      '../../../core/owt_base/RawTransport.cpp',
      '../../../core/owt_base/SctpTransport.cpp',
    ],
    'defines': [
            'NOMINMAX',
            '_WIN32_WINNT=0x0A00',
          ],
    "msvs_settings": {
          "VCCLCompilerTool": {
            'RuntimeTypeInfo': 'true',
            "ExceptionHandling": "1",
            'AdditionalOptions': ['/GR'], 
          },
      },
    'include_dirs': [
      '$(CORE_HOME)/common',
      '$(CORE_HOME)/owt_base',
      '$(CORE_HOME)/../../build/libdeps/build/include',
      'D:/workspace/vcpkg/installed/x64-windows-static/include',
      'D:/workspace/log4cxx/src/apache-log4cxx-0.10.0/src/main/include',
    ],
    'libraries': [
      '-lD:/workspace/vcpkg/installed/x64-windows-static/lib/boost_system-vc140-mt.lib',
      '-lD:/workspace/vcpkg/installed/x64-windows-static/lib/boost_thread-vc140-mt.lib',
      '-lD:/workspace/log4cxx/src/apache-log4cxx-0.10.0/projects/x64/Release/log4cxx',
      '-l$(CORE_HOME)/../../build/libdeps/usrsctp/vs/usrsctplib/Release/usrsctp.lib'
    ],
    # 'INET', 'INET6' flags must be added for usrsctp lib, otherwise the arguments of receive callback would shift
    'cflags_cc': ['-DINET', '-DINET6'],
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
  },
# not build test target
#  {
#    'target_name': 'SctpTest',
#    'type' : 'executable',
#    'sources': [
#      '../../../core/owt_base/RawTransport.cpp',
#      '../../../core/owt_base/SctpTransport.cpp',
#      '../../../core/owt_base/SctpTransportTest.cpp',
#    ],
#    'include_dirs': [
#      '$(CORE_HOME)/common',
#      '$(CORE_HOME)/owt_base',
#      '$(CORE_HOME)/../../third_party/usrsctp/usrsctplib'
#    ],
#    'libraries': [
#      '-lboost_system',
#      '-lboost_thread',
#      '-llog4cxx',
#      '-L$(CORE_HOME)/../../third_party/usrsctp/usrsctplib/.libs', '-lusrsctp',
#    ],
#    'conditions': [
#      [ 'OS=="mac"', {
#        'xcode_settings': {
#          'GCC_ENABLE_CPP_EXCEPTIONS': 'YES',        # -fno-exceptions
#          'MACOSX_DEPLOYMENT_TARGET':  '10.7',       # from MAC OS 10.7
#          'OTHER_CFLAGS': ['-g -O$(OPTIMIZATION_LEVEL) -stdlib=libc++']
#        },
#      }, { # OS!="mac"
#        'cflags!':    ['-fno-exceptions'],
#        'cflags_cc':  ['-Wall', '-O$(OPTIMIZATION_LEVEL)', '-g', '-std=c++11', '-DINET', '-DINET6'],
#        'cflags_cc!': ['-fno-exceptions']
#      }],
#    ]
#  }
  ]
}
