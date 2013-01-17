#!/bin/bash
set -e
LOGFILE=/var/log/gunicorn/senioritis.log
LOGDIR=$(dirname $LOGFILE)
NUM_WORKERS=3
USER=ngoke
GROUP=ngoke
cd /home/ngoke/Code/senioritis
test -d $LOGDIR || mkdir -p $LOGDIR
exec gunicorn_django -w $NUM_WORKERS \
  --user=$USER --group=$GROUP --log-level=debug \
  --log-file=$LOGFILE 2>>$LOGFILE
