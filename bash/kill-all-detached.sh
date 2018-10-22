#!/bin/bash

# for killing all detached screen sessions
# written by Ye Kyaw Thu
# date: 22 Oct 2018

screen -ls | grep Detached | cut -d. -f1 | sed 's/\t//' | xargs kill
