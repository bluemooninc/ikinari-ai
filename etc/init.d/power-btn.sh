#!/bin/bash
### BEGIN INIT INFO
# Provides:           bluemoon inc.
# Required-Start:
# Required-Stop:
# Default-Start:      2 3 4 5
# Default-Stop:       0 1 6
# Short-Description:
# Description:
### END INIT INFO
PIDFILE=/var/run/power-btn.pid
case "$1" in
     start)
        if [ -f $PIDFILE ]; then
           echo $PIDFILE exists.
           exit 1
        fi
        start-stop-daemon -S -x /usr/local/bin/power-btn/power-btn.py -b -m -p $PIDFILE
        ;;
     stop)
        if [ ! -f $PIDFILE ]; then
           echo $PIDFILE not found.
           exit 1
        fi
        start-stop-daemon -K -p $PIDFILE
        rm $PIDFILE
        ;;
     *)
        echo "Usage: /etc/init.d/power-btn {start|stop}"
        exit 1
        ;;
esac
exit 0
