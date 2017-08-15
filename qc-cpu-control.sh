adb shell root
adb shell setenforce 0
adb shell stop thermal-engine
adb shell rmmod core_ctl
#adb shell "echo 1 > /sys/devices/system/cpu/cpu1/online"
#adb shell "echo 1 > /sys/devices/system/cpu/cpu2/online"
adb shell "echo 0 > /sys/devices/system/cpu/cpu3/online"
#adb shell "echo performance > /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor"
#adb shell "echo performance > /sys/devices/system/cpu/cpu1/cpufreq/scaling_governor"
#adb shell "echo performance > /sys/devices/system/cpu/cpu2/cpufreq/scaling_governor"
#adb shell "echo performance > /sys/devices/system/cpu/cpu3/cpufreq/scaling_governor"

# monitor cpus status
#while true; 
#do
#	adb shell "cat /sys/devices/system/cpu/cpu*/online";
#	adb shell "cat /sys/devices/system/cpu/cpu*/cpufreq/scaling_cur_freq";
#	echo "========"; 
#	sleep 3;
#done
