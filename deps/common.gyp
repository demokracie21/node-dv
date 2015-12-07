{
  'target_defaults': {
    'conditions': [
      ['OS=="linux"',
        {
          'cflags_cc!': [ '-fno-exceptions' ],
          'cflags': [ '-O3', '-march=native', '-w' ],
        }
      ],
      ['OS=="mac"',
        {
          'xcode_settings': {
            'GCC_ENABLE_CPP_EXCEPTIONS': 'YES',
            'OTHER_CFLAGS': [ '-O3', '-march=native', '-w' ],
            'OTHER_CPLUSPLUSFLAGS' : ['-Wno-c++11-narrowing', '-std=c++11', '-stdlib=libc++'],
            'OTHER_LDFLAGS': ['-stdlib=libc++'],
          }
        }
      ],
      ['OS=="win"',
        {
          'defines!': ['_HAS_EXCEPTIONS=0'],
          'configurations': {
            'Debug': {
              'msvs_settings': {
                'VCCLCompilerTool': {
                  'ExceptionHandling': '1',
                },
              },
            },
            'Release': {
              'msvs_settings': {
                'VCCLCompilerTool': {
                  'WarningLevel': '0',
                  'ExceptionHandling': '1',
                },
              },
            },
          },
        }
      ]
    ]
  }
}
