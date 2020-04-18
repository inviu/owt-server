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
                      'D:/workspace/vcpkg/installed/x64-windows-static/include',
                      'D:/workspace/log4cxx/src/apache-log4cxx-0.10.0/src/main/include',
                    ],               
    'libraries': [
      '-lD:/workspace/vcpkg/installed/x64-windows-static/lib/boost_thread-vc140-mt.lib',
      '-lD:/workspace/log4cxx/src/apache-log4cxx-0.10.0/projects/x64/Release/log4cxx',
      '-lD:/workspace/owt-server/source/core/../../build/libdeps/build/bin/avutil',
      '-lD:/workspace/owt-server/source/core/../../build/libdeps/build/bin/avcodec',
      '-lD:/workspace/owt-server/source/core/../../build/libdeps/build/bin/avformat',
      '-lD:/workspace/owt-server/source/core/../../build/libdeps/build/bin/swresample',
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
