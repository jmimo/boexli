#!/usr/bin/env bash

ln -s output.sh /etc/init.d/boexli-output
chmod +x /etc/init.d/boexli-output
update-rc.d /etc/init.d/boexli-output defaults
