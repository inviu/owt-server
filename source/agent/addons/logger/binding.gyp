{
  'targets': [{
    'target_name': 'logger',
    'sources': [
      'addon.cc'
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
      '$(CORE_HOME)/../../third_party/log4cxx/src/apache-log4cxx-0.10.0/src/main/include',
      "<!(node -e \"require('nan')\")"
    ],
    'library_dirs': [
      '$(CORE_HOME)/../../third_party/lib',
    ],    
    'libraries': [
      '-llog4cxx',
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
  },
  ]
}
