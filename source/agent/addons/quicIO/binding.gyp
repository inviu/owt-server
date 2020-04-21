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
            'WIN32_LEAN_AND_MEAN',
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
      '$(CORE_HOME)/../../third_party/boost_1.72.0/include',
    ],
    'libraries': [
      '-llibboost_thread-vc141-mt-s-x64-1_69.lib',
      '-llibboost_system-vc141-mt-s-x64-1_69.lib',
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
