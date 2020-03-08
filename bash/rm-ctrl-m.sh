#!/bin/bash

# for removing CTRL+M or ^M characters
#
# Windows-based text editors will have a special carriage return character (CR+LF)
# at the end of lines to denote a line return or newline,
# which will be displayed incorrectly in Linux "^M"
#
# Here, demo of calling perl one liner inside bash shell script for students
# In the real world, we used several combinations of shell and perl for NLP pre and post processings
# 
# How to run: bash rm.ctrl-m.sh <input-file> > <output-file>
# e.g. bash rm.ctrl-m.sh ./yandex.en-th.seg > yandex.en-th.seg.unix

# before removing, inside yandex.en-th.seg file:
# ใช่/ฉัน/ชอบ/เล่น/เป็น/ไทย/หมากรุก/หรอก/^M/
# คุณ/สามารถ/ขอ/แนะนำ/บาง/อย่าง/สำหรับ/เด็ก/?/^M/
# ยังไง/ฉัน/ไป/อยู่/ที่/นั่น/?/^M/
#
# after removing, inside yandex.en-th.seg.unix file:
# ใช่/ฉัน/ชอบ/เล่น/เป็น/ไทย/หมากรุก/หรอก//
# คุณ/สามารถ/ขอ/แนะนำ/บาง/อย่าง/สำหรับ/เด็ก/?//
# ยังไง/ฉัน/ไป/อยู่/ที่/นั่น/?//
 
perl -p -e 's/\r//g' $1 > $1.unix
