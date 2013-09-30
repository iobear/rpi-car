#!/bin/bash
### BEGIN INIT INFO
# Provides: dualShock
# Required-Start:    $local_fs bluetooth
# Required-Stop:     $local_fs
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Start dualshock motor controller
### END INIT INFO
#
# set -e

PATH=/bin:/usr/bin:/sbin:/usr/sbin
DAEMON=/usr/local/bin/dualShock.py

dualShock_already_running_check () {
	ps -e | grep dualShock.py > /dev/null
}

. /lib/lsb/init-functions

case "$1" in
	start)
if (dualShock_already_running_check "$1"); then
	log_warning_msg "dualShock is already running"
else {
		while true; do
				#waiting for the controller to be connected
				if [ -a /dev/input/js0 ]; then
						python $DAEMON &>>/var/log/dualShock &
						break
				else
						sleep 1
						#echo "waiting..."
				fi
		done
}
fi
		;;
	stop)
			killall dualShock.py
		;;
	*)
		echo "Usage: /etc/init.d/dualShock.sh {start|stop}" >&2
		exit 1
		;;
esac

exit 0