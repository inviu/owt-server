{
  'targets': [{
    'target_name': 'sipIn',
    'sources': [
      'addon.cc',
      'SipGateway.cc',
      'SipCallConnection.cpp',
      'AudioFrameConstructorWrapper.cc',
      'AudioFramePacketizerWrapper.cc',
      'VideoFrameConstructorWrapper.cc',
      'VideoFramePacketizerWrapper.cc',
      '../../addons/common/NodeEventRegistry.cc',
      '../../../core/owt_base/AudioFrameConstructor.cpp',
      '../../../core/owt_base/AudioFramePacketizer.cpp',
      '../../../core/owt_base/AudioUtilities.cpp',
      '../../../core/owt_base/MediaFramePipeline.cpp',
      '../../../core/owt_base/VideoFrameConstructor.cpp',
      '../../../core/owt_base/VideoFramePacketizer.cpp',
      '../../../core/owt_base/SsrcGenerator.cc',
      '../../../core/rtc_adapter/VieReceiver.cc',
      '../../../core/rtc_adapter/VieRemb.cc' #20150508
    ],
    'dependencies': ['sipLib'],
    'cflags_cc': ['-DWEBRTC_POSIX', '-DWEBRTC_LINUX'],
    'defines': [
            'NOMINMAX',
            '_WIN32_WINNT=0x0A00',
            'WIN32_LEAN_AND_MEAN',
            'WEBRTC_WIN',
          ],
    "msvs_settings": {
          "VCCLCompilerTool": {
            'RuntimeTypeInfo': 'true',
            "ExceptionHandling": "1",
            'AdditionalOptions': ['/GR','/FI\"winsock2.h\"','/FI\"windows.h\"']
          },
      },
    'include_dirs': [
      '../../../core/common',
      '../../../core/owt_base',
      '../../../core/rtc_adapter',
      '../../../../third_party/licode/erizo/src/erizo',
      '../../../../third_party/webrtc/src',
    ],
    'library_dirs': [
      'D:/workspace/owt-server/source/core/../../build/libdeps/build/lib',
      '-llibboost_thread-vc141-mt-s-x64-1_69.lib',
      '$(CORE_HOME)/../../third_party/lib',
    ],
    'libraries': [
      # '-L$(CORE_HOME)/../../third_party/webrtc', '-lwebrtc',
      '-lD:/workspace/owt-server/source/core/../../third_party/webrtc/webrtc',
      '-llog4cxx',
      '-lboost_thread',
      '-lboost_system',
      # Add following arguments to help ldd find libraries during packing
      # '-L$(CORE_HOME)/../../build/libdeps/build/lib',
      # '-lre',
      # '-Wl,-rpath,<!(pwd)/build/$(BUILDTYPE)',
    ],
    'conditions': [
      [ 'OS=="mac"', {
        'xcode_settings': {
          'GCC_ENABLE_CPP_EXCEPTIONS': 'YES',        # -fno-exceptions
          'MACOSX_DEPLOYMENT_TARGET':  '10.7',       # from MAC OS 10.7
          'OTHER_CFLAGS': ['-g -O3 -stdlib=libc++']
        },
      }, { # OS!="mac"
        'cflags!':    ['-fno-exceptions'],
        'cflags_cc':  ['-Wall', '-O3', '-g' , '-std=c++11'],
        'cflags_cc!': ['-fno-exceptions']
      }],
    ]
  },
  {
    'target_name': 'sipLib',
    'type': 'shared_library',
    'sources': [
        'sip_gateway/SipEP.cpp',
        'sip_gateway/SipGateway.cpp',
        'sip_gateway/SipCallConnection.cpp',
    ],
    'direct_dependent_settings': {
        'include_dirs': ['sip_gateway'],
    },
    'defines': [
            'NOMINMAX',
            '_WIN32_WINNT=0x0A00',
            'WIN32_LEAN_AND_MEAN',
            'USE_VIDEO',
            'USE_TLS',
            '__STDC__',
          ],
    "msvs_settings": {
          "VCCLCompilerTool": {
            'RuntimeTypeInfo': 'true',
            "ExceptionHandling": "1",
            'AdditionalOptions': ['/GR','/FI\"winsock2.h\"','/FI\"windows.h\"']
          },
      },
    'include_dirs': [
        'sip_gateway',
        'sip_gateway/sipua/include',
        '$(CORE_HOME)/common',
        '../../../../third_party/licode/erizo/src/erizo',
        '$(CORE_HOME)/../../build/libdeps/build/include',
        '$(CORE_HOME)/../../third_party/boost_1.72.0/include',
        '$(CORE_HOME)/../../third_party/log4cxx/src/apache-log4cxx-0.10.0/src/main/include',
    ],
    'library_dirs': [
      '$(CORE_HOME)/../../build/libdeps/build/lib',
      '-llibboost_thread-vc141-mt-s-x64-1_69.lib',
      '$(CORE_HOME)/../../third_party/lib',
      'build/release',
    ],
    'libraries': [
        '-llibsipua',
        # '-L$(CORE_HOME)/../../build/libdeps/build/lib',
        '-lre-win32',
        '-llog4cxx',
        '-lboost_thread-vc140-mt.lib',
        '-lboost_system-vc140-mt.lib',
        '-lpthreadVC3',
        '-lIphlpapi',
    ],
    'conditions': [
      [ 'OS=="mac"', {
        'xcode_settings': {
          'GCC_ENABLE_CPP_EXCEPTIONS': 'YES',        # -fno-exceptions
          'MACOSX_DEPLOYMENT_TARGET':  '10.7',       # from MAC OS 10.7
          'OTHER_CFLAGS': ['-g -O3 -stdlib=libc++']
        },
      }, { # OS!="mac"
        'cflags!':    ['-fno-exceptions'],
        'cflags_cc':  ['-Wall', '-O3', '-g', '-std=c++0x'],
        'cflags_cc!': ['-fno-exceptions']
      }],
    ],
    # 'actions': [
    #   {
    #     'action_name': 'sipua_build',
    #     'inputs': [
    #       '<!@(find <!(pwd)/sip_gateway/sipua -type f -name "*.h")',
    #       '<!@(find <!(pwd)/sip_gateway/sipua -type f -name "*.c")',
    #     ],
    #     'outputs': [
    #       '<!(pwd)/sip_gateway/sipua/libsipua.a'
    #     ],
    #     'action': ['eval', 'cd <!(pwd)/sip_gateway/sipua && make clean && make RE_HOME=$(CORE_HOME)/../../build/libdeps/build'],
    #   }
    # ]
  },
  {
    'target_name': 'libsipua',
    'type': 'static_library',
    'sources': [
        # 'sip_gateway/sipua/modules/dtls_srtp/dtls.c',
        # 'sip_gateway/sipua/modules/dtls_srtp/dtls_srtp.c',
        # 'sip_gateway/sipua/modules/dtls_srtp/dtsrtp.c',
        'sip_gateway/sipua/modules/ice/ice.c',
        'sip_gateway/sipua/modules/natpmp/libnatpmp.c',
        'sip_gateway/sipua/modules/natpmp/natpmp.c',
        'sip_gateway/sipua/modules/srtp/sdes.c',
        'sip_gateway/sipua/modules/srtp/srtp.c',
        'sip_gateway/sipua/modules/stun/stun.c',
        'sip_gateway/sipua/modules/turn/turn.c',
        # 'sip_gateway/sipua/modules/zrtp/zrtp.c',
        'sip_gateway/sipua/src/account.c',
        'sip_gateway/sipua/src/aucodec.c',
        'sip_gateway/sipua/src/audio.c',
        'sip_gateway/sipua/src/bfcp.c',
        'sip_gateway/sipua/src/call.c',
        'sip_gateway/sipua/src/conf.c',
        'sip_gateway/sipua/src/log.c',
        'sip_gateway/sipua/src/mctrl.c',
        'sip_gateway/sipua/src/menc.c',
        'sip_gateway/sipua/src/metric.c',
        'sip_gateway/sipua/src/mnat.c',
        # 'sip_gateway/sipua/src/mock_sip_gateway.c',
        'sip_gateway/sipua/src/net.c',
        'sip_gateway/sipua/src/realtime.c',
        'sip_gateway/sipua/src/reg.c',
        'sip_gateway/sipua/src/rtpkeep.c',
        'sip_gateway/sipua/src/sdp.c',
        'sip_gateway/sipua/src/sipreq.c',
        'sip_gateway/sipua/src/sipua.c',
        'sip_gateway/sipua/src/sipua_actions.c',
        'sip_gateway/sipua/src/stream.c',
        'sip_gateway/sipua/src/ua.c',
        'sip_gateway/sipua/src/uag.c',
        'sip_gateway/sipua/src/vidcodec.c',
        'sip_gateway/sipua/src/video.c',
    ],
    'direct_dependent_settings': {
        'include_dirs': ['sip_gateway'],
    },
    'defines': [
            'NOMINMAX',
            '_WIN32_WINNT=0x0A00',
            'WIN32_LEAN_AND_MEAN',
            'USE_VIDEO',
            'USE_TLS',
            '__STDC__',
          ],
    "msvs_settings": {
          "VCCLCompilerTool": {
            'RuntimeTypeInfo': 'true',
            "ExceptionHandling": "1",
            'AdditionalOptions': ['/GR','/FI\"winsock2.h\"','/FI\"windows.h\"']
          },
      },
    'include_dirs': [
        'sip_gateway',
        'sip_gateway/sipua/include',
        '$(CORE_HOME)/common',
        '../../../../third_party/licode/erizo/src/erizo',
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
        # '-L<!(pwd)/sip_gateway/sipua', '-lsipua',
        # '-L$(CORE_HOME)/../../build/libdeps/build/lib',
        '-lre-win32',
        '-llog4cxx',
        '-lboost_thread-vc140-mt.lib',
        '-lboost_system-vc140-mt.lib',
        '-lpthreadVC3',
    ],
  },
  ]
}
