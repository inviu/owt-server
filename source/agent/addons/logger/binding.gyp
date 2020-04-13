{
  'targets': [{
    'target_name': 'logger',
    'sources': [
      'addon.cc'
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
      'D:/workspace/log4cxx/src/apache-log4cxx-0.10.0/src/main/include',
      "<!(node -e \"require('nan')\")"
    ],
    'libraries': [
      '-lD:/workspace/log4cxx/src/apache-log4cxx-0.10.0/projects/x64/Release/log4cxx',
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
