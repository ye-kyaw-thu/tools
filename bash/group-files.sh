#!/bin/bash

# for grouping a large number of files
# written by Ye Kyaw Thu, NECTEC, Thailand
# how to run: ./group-files.sh 100

# if you want to recursively copy batch of 100 files, give 100
batchSize=$1;

#Read folders and put them into folderArray variable
folderArray=($(ls -ad */));

for class in "${folderArray[@]}"
do
   fileArray=($(ls ${class}*jpg));
   group=1;
   counter=1;
   subFolder=${class::-1}_${group};

   mkdir $class$subFolder;

   for conFile in "${fileArray[@]}"
   do

      if [ $counter -gt $batchSize ]; then
         
         counter=1;
         group=$((group + 1));
         subFolder=${class::-1}_${group};
         
         mkdir $class$subFolder; 

      fi
      
      echo -e "cp $conFile $class$subFolder/\n";
      cp $conFile $class$subFolder/;

      let counter++;
  done;
done
