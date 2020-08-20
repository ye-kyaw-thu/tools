#!/bin/bash

# listing installed Myanmar language font files on your Linux machine
# written by Ye Kyaw Thu, LST, NECTEC, Thailand
# Reference: man fc-list
# How to run: ./my-font-chk.sh

# fc-list :lang=my
fc-list -f '%{file}\n' :lang=my
