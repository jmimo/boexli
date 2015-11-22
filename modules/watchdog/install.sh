#!/usr/bin/env bash

ln -s watchdog.sh /etc/init.d/boexli-watchdog
chmod +x /etc/init.d/boexli-watchdog
update-rc.d /etc/init.d/boexli-watchdog defaults
