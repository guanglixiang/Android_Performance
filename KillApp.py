#!/usr/bin/env python
'''
@author: guanglixiang@gmail.com
@summary: this script use to kill app
'''
import argparse
import inspect
import sys
import commands

def killApp(keyword):
    findPackCmd = "adb shell ps|grep %s|awk {'print $9'}" % (keyword)
    packName = commands.getoutput(findPackCmd)
    if len(packName) == 0:
        print "running packages name include %s not found!" % (keyword)
        sys.exit()
    for pro in packName.split("\n"):
        if ":" in pro:
            getProcCmd = "adb shell ps|grep %s|awk {'print $2'}" % (pro.split(":")[0])
        else:
            getProcCmd = "adb shell ps|grep %s|awk {'print $2'}" % (pro)
        proc = commands.getoutput(getProcCmd)
        killCmd = 'adb shell kill %s' % (proc)
        killStatus = commands.getstatusoutput(killCmd)[0]
        if killStatus != 0:
            print "kill %s failure!" % (pro) 
def parse_args():
    parser = argparse.ArgumentParser(
        description=inspect.getdoc(sys.modules[__name__]),
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('-p', help='key words in package name which you want killed')
    return parser.parse_args()

def main():
    args = parse_args()
    killApp(args.p)

if __name__ == '__main__':
    main()