#!/bin/bash

iptables -A INPUT -s 192.168.1.1 -j DROP

touch /var/log/snort/snort.log
