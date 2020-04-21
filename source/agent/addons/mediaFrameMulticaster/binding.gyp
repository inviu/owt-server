{
  'targets': [{
    'target_name': 'mediaFrameMulticaster',
    'sources': [
      'addon.cc',
      'MediaFrameMulticasterWrapper.cc',
      '../../../core/owt_base/MediaFrameMulticaster.cpp',
      '../../../core/owt_base/MediaFramePipeline.cpp',
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
    'include_dirs': ['$(CORE_HOME)/common',
                      '$(CORE_HOME)/owt_base',
                      '$(CORE_HOME)/../../third_party/boost_1.72.0/include',
                      ],
    'library_dirs': [
      '$(CORE_HOME)/../../third_party/boost_1.72.0/lib/windows/x64/release',
    ],    
    'libraries': [
      '-lboost_thread-vc140-mt.lib',
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
