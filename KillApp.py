#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
'''
@author: guanglixiang@gmail.com
@summary: this script use to kill app
'''
'''
一条shell语句搞定本脚本:adb shell kill `adb shell ps|grep <keyword>|awk {'print $2'}`，
但它不够通用。
解除脚本运行主机shell环境的依赖，让脚本只依赖python跟adb，win环境下也可以运行。
'''
import argparse
import inspect
import os
import sys
import collections
import device

def check_env(device):
    '''
    we must have root permission
    '''
    if device.get_prop('ro.secure') == '0':
        return True
    else:
        return False
    
def get_be_killed_apps(device, keyword):
    stdout, stderr = device.shell(['ps'])
    pkg_pids = collections.defaultdict(list)
    for line in stdout.split("\n"):
        if len(line) <= 0:
            break
        ps_data = line.split()
        if keyword in ps_data[-1]:
            pid, pkg = ps_data[1], ps_data[-1]
            pkg_pids[pkg].append(pid)
    return pkg_pids

def kill_app(device, pkg_pid):
    for name, ids in pkg_pid.iteritems():
        stdout, stderr = device.shell(['kill', ids[0]])
        if len(stdout) <= 0:
            print "kill %s succeed" % name
    sys.exit()

def parse_args():
    parser = argparse.ArgumentParser(
        description=inspect.getdoc(sys.modules[__name__]),
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('-k', help='key words in package name which you want killed')
    parser.add_argument('-s', '--serial', default=os.getenv('ANDROID_SERIAL'),
                        help='Adb device serial number.')
    return parser.parse_args()

def main():
    args = parse_args()
    dev = device.get_device(args.serial)
    if not check_env(dev):
        print "You must have root permission"
        sys.exit()
    kill_app(dev, get_be_killed_apps(dev, args.k))

if __name__ == '__main__':
    main()
