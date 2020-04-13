{
  'targets': [{
    'target_name': 'quicIO',
    'sources': [
      'addon.cc',
      'QuicTransport.cc',
      'InternalQuic.cc',
      '../../../core/owt_base/MediaFramePipeline.cpp'
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
      "<!(node -e \"require('nan')\")",
      '../../../core/owt_base',
      '../../../agent/addons/common',
      '../../../../third_party/quic-lib/dist/include',
      'D:/workspace/vcpkg/installed/x64-windows-static/include',
    ],
    'libraries': [
      '-lD:/workspace/vcpkg/installed/x64-windows-static/lib/boost_system-vc140-mt.lib',
      '-lD:/workspace/vcpkg/installed/x64-windows-static/lib/boost_thread-vc140-mt.lib',
      '-L<(module_root_dir)/../../../../third_party/quic-lib/dist/lib',
      '-lrawquic'
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
