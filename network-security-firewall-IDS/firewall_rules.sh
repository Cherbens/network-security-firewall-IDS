#!/bin/bash

# Example firewall rule to block a specific IP
iptables -A INPUT -s 192.168.1.1 -j DROP

# Log suspicious traffic
touch /var/log/snort/snort.log