# Copyright (C) <2018> Intel Corporation
#
# SPDX-License-Identifier: Apache-2.0

'''Script to build WebRTC libs on Windows.

It builds libics which includes WebRTC lib, WooGeen base, p2p and conference
lib.

Output lib is located in out/ics.lib.
'''

import os
import sys
import subprocess
import argparse

HOME_PATH = os.path.abspath(os.path.dirname(__file__))
LIBS_PATH= os.path.join(HOME_PATH, '../webrtc/src/out')
LIB_PATH=r'C:\Program Files (x86)\Microsoft Visual Studio\2017\Professional\VC\Tools\MSVC\14.16.27023\bin\Hostx64\x64\lib.exe'
OUT_LIB = 'webrtc.lib'


def _getlibs(scheme):
  '''Returns an array contains all .lib files' path
  '''
  root_path = os.path.join(LIBS_PATH, scheme)
  result = []
  for root, _, files in os.walk(root_path):
    for file in files:
      name, ext = os.path.splitext(file)
      if(ext=='.lib'):
        result.append(os.path.abspath(os.path.join(root, file)))
        # print('Merged {}.lib',name)
  return result

def _mergelibs(scheme):
  if os.path.exists(OUT_LIB):
    os.remove(OUT_LIB)
  libs=_getlibs(scheme)
  dst='/OUT:'+os.path.join(HOME_PATH,OUT_LIB)
  command=[LIB_PATH, dst]
  command.extend(libs)
  subprocess.call(command, cwd=HOME_PATH)


def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('--scheme', default='obj',
    help='Schemes for building. Supported value: debug, release')
  opts=parser.parse_args()
  _mergelibs(opts.scheme)
  print('Done')
  return 0

if __name__ == '__main__':
  sys.exit(main())
