#!/usr/bin/env python
'''
@author: guanglixiang@gmail.com
@summary: this script use to test launch activity time
'''
from commands import getoutput
from time import sleep
from __builtin__ import int

LAUNCH_PACKAGE = 'com.tct.email'
LAUNCH_ACTIVITY = 'com.tct.email/.activity.Welcome'
TEST_COUNT = 5
SLEEP_TIME = 10

LOG_LINE = "**************************************************"

def getVerInfo():
   getVerCmd = "adb shell dumpsys package %s | grep version" % (LAUNCH_PACKAGE)
   verinfo = getoutput(getVerCmd)
   print LOG_LINE
   print "Test APK version info is:"
   print verinfo.strip()
   print LOG_LINE

def getLaunchTime():
    getLaunchTimeCmd = "adb shell am start -W -S %s |grep TotalTime|awk '{print $2}'" % (LAUNCH_ACTIVITY)
    totalTime = 0
    for i in range(1, TEST_COUNT ＋ 1):
        time = getoutput(getLaunchTimeCmd)
        print "%s lunch time is %s" % (i, time)
        totalTime += int(time)
        if (i < TEST_COUNT):
            sleep(SLEEP_TIME)
        i = i + 1
    average = totalTime / TEST_COUNT
    print "%s launch time average is %s" % (TEST_COUNT, average)

def main():
    getVerInfo()
    getLaunchTime()

if __name__ == '__main__':
    main()
        
