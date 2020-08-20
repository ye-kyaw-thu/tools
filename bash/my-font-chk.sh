#!/bin/bash

# listing installed Myanmar language fonts on your Linux machine
# written by Ye Kyaw Thu, LST, NECTEC, Thailand
# Reference: man fc-list
# How to run: ./my-font-chk.sh

fc-list -f '%{file}\n' :lang=my
