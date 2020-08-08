#!/bin/bash

# Demo shell script of getting date, time information
# Written by Ye Kyaw Thu, LST Lab., NECTEC, Thailand
# Last updated: 8 Aug 2020
# How to run: bash ./date-time-info.sh


Day=`date +%d`;
Month=`date +%m`;
Year=`date +%Y`;
mmWeekday=`date +%A`;

Hour=`date +%H`;
Minute=`date +%M`;
Second=`date +%S`;

#  %x   locale's date representation (e.g., 12/31/99)
localDate=`date +%x`;

#  %X   locale's time representation (e.g., 23:13:48)
#localTime=`date +%X`;

#  %r   locale's 12-hour clock time (e.g., 11:11:04 PM)
localTime12=`date +%r`;

#  %R   24-hour hour and minute; same as %H:%M
localTime24=`date +%r`;

#  %B   locale's full month name (e.g., January)
localMonth=`date +%B`;

#  %c   locale's date and time (e.g., Thu Mar  3 23:05:25 2005)
localDateTime=`date +%c`;

echo "Output of the date command:";
echo `date`;
echo "==========";

echo "Current local's date is: $localDate";
echo "Current local's 12-hour clock time is: $localTime12";
echo "Current local's 24-hour hour and minute is: $localTime24";

echo "Current Date: $Day ရက် $Month လ $Year ခုနှစ် ($mmWeekdayနေ့)";
echo "Current Time: $Hour နာရီ $Minute မိနစ် $Second စက္ကန့်";

echo "Current local month: $localMonth";
echo "Current local date and time: $localDateTime";
echo "=========="

#To print the date of the day before yesterday:
twoDaysAgo=`date --date='2 days ago'`;
echo "The date of the day before yesterday: $twoDaysAgo";

#To print the date of the day three months and one day hence:
SixMonthFifteenDay=`date --date='6 months 15 day'`;
echo "The date of the day six months and 15 day: $SixMonthFifteenDay";

#To print the day of year of Christmas in the current year:
ChristmasDate=`date --date='25 Dec' +%j`;
echo "The day of year of Christmas in the current year: $ChristmasDate";

#Someone's birthday
yBirthday=`date --date='25 April' +%x`;
echo "Someone's Birthday in the current year: $yBirthday";


