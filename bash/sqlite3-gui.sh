#!/bin/bash

# for applying zenity GUI together with a sqlite3 database
# written by Ye Kyaw Thu, LST, NECTEC, Thailand
# last updated: 26 Feb 2021
#
# Note: --width 500 -- height 300 ရဲ့ နောက်မှာ --extra-button ကို သွားထားရင် button က ပြမပေးနိုင်တာကို တွေ့ရ...
#  --form အတွက်က --no-cancel ကို သုံးပြီး cancel button ကို ဖျောက်လို့ မရဘူး။ "--no-cancel is not supported for this dialog" ဆိုပြီး error message ပေးလိမ့်မယ်။
# ပြီးတော့ ဒီ zenity+bash+sqlite3 က မြန်မာ CS ကျောင်းသားတွေအတွက် bash နဲ့လည်း လွယ်လွယ်ကူကူ database application အသေးစားလေးကို လုပ်နိုင်ကြောင်း 
# အချိန်တရက်လောက်ပဲ ယူပြီး ရေးပြထားတဲ့ ဒီမို ပရိုဂရမ်လေး ဖြစ်လို... User Interface, Usability အပိုင်းက ကြည့်ရင် ပြောစရာတွေ ရှိပါတယ်။ 
# ဥပမာ... မရှိတဲ့ ID ကို ရိုက်ထည့်တဲ့အခါမှာ အဲဒီ ID က မရှိဘူး စသည်ဖြင့် Error message ပေးတာမျိုးကို လုပ်မထားပါဘူး။
# သို့သော် လွန်ခဲ့တဲ့ နှစ်၂၀ကျော်လောက်က NCC IDCS Diploma ရဲ့ ပရောဂျက်တစ်ခုအနေနဲ့ C programming language နဲ့ အခုလို အလုပ်ကို 
# file input/output (ဆိုလိုတာက database မဟုတ်) နဲ့ Dos OS ပေါ်မှာပဲ ASCII Character တွေကိုပဲ သုံးပြီး GUI ကို ဖန်တီးပြီး လုပ်ခဲ့ရပါတယ်။
# အဲဒီအတွက် တကယ်က ၂လ၊ ၃လ လောက်ကို အချိန်ယူပြီး ခက်ခက်ခဲခဲ လုပ်ခဲ့ကြရတာပါ။
# ဒီလောက်သပ်ရပ်တဲ့ GUI မျိုးလည်း ရခဲ့တာ မဟုတ်ကြောင်းကို လက်ရှိ CS ကျောင်းသားတွေကို သိစေချင်တာကြောင့်လည်း ဒီ ဒီမိုဂရိုဂရမ်ကို ရေးဖြစ်ခဲ့တာပါ။
# 
# reference: zenity --help-all
# reference: https://askubuntu.com/questions/690818/building-a-dynamic-zenity-list-using-bash-variable
# reference: https://stackoverflow.com/questions/37997249/zenity-dialog-window-with-two-buttons-but-no-text-entry
# reference: https://stackoverflow.com/questions/27371765/importing-csv-file-to-sqlite3-db-table
# reference: https://medium.com/swlh/how-to-insert-data-from-csv-file-into-a-sqlite-database-using-python-82f7d447866a


# function for listing all records
function dumpDB() {

reply=1;

# OK button က zero, ကျန်တဲ့ button တွေအားလုံးက 1 ပဲ return ပြန်တယ်။ အဲဒါကြောင့် 1 ဖြစ်နေသ၍ looping ပတ်ခိုင်းထားတာ...
while [ $reply -eq 1 ];  do
#   sqlite3 student.db "SELECT * FROM candidate;" | sed  's/\n/ /g;' | sed 's/|/\n/g;' | zenity --list --title "Language Understanding Lab." --text "Student Database" --column "ID" --column "Name" --column "Age" --column "Research Field" --column "University" --column "Class" --width 800 --height 300 --cancel-label 'Add' --ok-label 'Quit'

#   recno=$(sqlite3 student.db "SELECT * FROM candidate;" | sed  's/\n/ /g;' | sed 's/|/\n/g;' | zenity --list --title "Language Understanding Lab." --text "Student Database" --column "ID" --column "Name" --column "Age" --column "Research Field" --column "University" --column "Class" --width 800 --height 300 --cancel-label 'Add' --ok-label 'Quit' );
   ans=$(sqlite3 student.db "SELECT * FROM candidate;" | sed  's/\n/ /g;' | sed 's/|/\n/g;' | zenity --list --editable --title "Language Understanding Lab." --text "Student Database" --column "ID" --column "Name" --column "Age" --column "Research Field" --column "University" --column "Class" --width 800 --height 400 --ok-label 'Quit' --cancel-label 'Add' --extra-button 'Delete' --extra-button 'Edit' );
   reply=$?; check="${reply}-${ans}"; echo $check;
   
   case $check in
      '1-' ) # for adding a new record
      record=$(zenity --forms --title "New Student Form" --add-entry="Name" --add-entry="Age" --add-entry="Research Field" --add-entry="University" --add-entry="Class" --width 500 -- height 300);
      formattedRecord=$(echo $record | sed "s/|/\',\'/g;" | sed "s/^/\'/" | sed "s/$/\'/"); 
      echo $formattedRecord;
      sqlite3 student.db "INSERT INTO candidate (name, age, field, univ, class) VALUES ($formattedRecord);"
      ;;
      '1-Delete' ) # for delection a record with the ID
      id=$(zenity --entry --title "Delete Form" --text "ID No.:");
      sqlite3 student.db "DELETE FROM CANDIDATE WHERE ID = $id;"
      ;;
      '1-Edit' ) # for editing records
      # dumping database as CSV format
      sqlite3 -header -csv ./student.db "select * from candidate;" | tr "," "|" > student.csv
      # backup the original database
      # ဒီနေရာမှာ တကယ်လို့ cp မလုပ်ပဲ mv လုပ်ခဲ့ရင် ပြဿနာတစ်ခုဖြစ်လာပါလိမ့်မယ်။ ဘယ်အချိန်မှာလဲ ဆိုရင် user က Cancel button ကို နှိပ်တဲ့အခါမှာပါ။
      cp ./student.db ./student.backup;
      data=$(cat ./student.csv);
      # allow user to edit the whole database as a CSV text file, တစ်ခု သတိထားရမှာက "," ပါတဲ့ field တွေကို double quote အတွင်းမှာ ရေးပေးရပါမယ်
      # ဘာကြောင့်လည်း ဆိုတော့ database ကိုယ်တိုင်ကလည်း comma နဲ့ field တွေကို ခွဲခြားတာမို့ပါ။
      newData=$(echo -n "$data" | zenity --text-info --title "Database Editing Form" --editable --width 650 --height 400)
      rc=$?;
      if [ $rc -eq 0 ]
      then
         echo "$newData" | tr "|" "," > student.csv; # ဒီနေရာမှာ bash script ရဲ့ trick လို့ ပြောရမလား $newData နဲ့ "$newData" နဲ့က မတူပါဘူး
         #cat student.csv; # just for debugging...
         # deleting the original student.db database
         rm student.db;
         # creating a new database with the updated data
         sqlite3 -separator ',' student.db ".import student.csv candidate";
      fi
   esac
   
done
}

# ဒီ if က student.db က လက်ရှိ bash script ကို run တဲ့ path အောက်မှာရှိထားပြီးသားလားဆိုပြီး စစ်တာပါ။
# ရှိခဲ့ရင် database ကို dump လုပ်ပြီး zenity GUI တစ်ခုဖြစ်တဲ့ list မှာ ပြပေးပါလိမ့်မယ်။
# တကယ်လို့ student.db လို့ နာမည်ပေးထားတဲ့ database က အဆင်သင့် မရှိသေးရင်တော့ 
# else အောက်ကို ဝင်သွားပြီးတော့ example database ကို တည်ဆောက်ပြီးမှ database ကို dump လုပ်ပါလိမ့်မယ်။
if [ -f student.db ]
then
   dumpDB;
else
   sqlite3 student.db "CREATE TABLE candidate (id INTEGER PRIMARY KEY, name TEXT NOT NULL, age INTEGER NOT NULL, field CHAR(50), univ CHAR(80), class CHAR(30));"
   sqlite3 student.db  "INSERT INTO candidate (name, age, field, univ, class) VALUES ('Zar Zar', 26, 'Machine Translation (MT)', 'KMITL, Thailand', 'PhD Candidate');"
   sqlite3 student.db  "INSERT INTO candidate (name, age, field, univ, class) VALUES ('Hlaing Myat', 25, 'SignWriting', 'UTYCC, Myanmar', 'PhD Candidate');"
   sqlite3 student.db  "INSERT INTO candidate (name, age, field, univ, class) VALUES ('Zun Hlaing', 25, 'Myanmar Braille MT', 'UTYCC, Myanmar', 'PhD Candidate');"   
   sqlite3 student.db  "INSERT INTO candidate (name, age, field, univ, class) VALUES ('Ni Htwe', 30, 'Myanmar Fingerspelling', 'YTU, Myanmar', 'PhD Candidate');"
   sqlite3 student.db  "INSERT INTO candidate (name, age, field, univ, class) VALUES ('Thazin', 32, 'Burmese Dialect Machine Translation', 'UCSY, Myanmar', 'PhD Candidate');"
   sqlite3 student.db  "INSERT INTO candidate (name, age, field, univ, class) VALUES ('Myo Mar', 21, 'Text to Speech (TTS)', 'UTYCC, Myanmar', 'MSc Student');"
   sqlite3 student.db  "INSERT INTO candidate (name, age, field, univ, class) VALUES ('Hayman', 24, 'Pao Language Processing', 'UTYCC, Myanmar', 'MSc Student');"   
   sqlite3 student.db  "INSERT INTO candidate (name, age, field, univ, class) VALUES ('Mya Ei', 21, 'Under-resourced Machine Translation', 'SIIT, Thailand', 'MSc Student');"
   sqlite3 student.db  "INSERT INTO candidate (name, age, field, univ, class) VALUES ('Theingi', 26, 'Burmese Romanization', 'YTU, Myanmar', 'MSc Student');"
   sqlite3 student.db  "INSERT INTO candidate (name, age, field, univ, class) VALUES ('Shwe Sin', 26, 'Text to Speech (TTS)', 'YTU, Myanmar', 'MSc Student');"   
   dumpDB;   
fi
