#!/bin/bash

## Written by Ye Kyaw Thu,
## Affiliate Professor, IDRI, CADT, Cambodia
## Evaluation with chrF++ score for all hypothesis files
## Last Updated: 07 June 2022

#MODEL_FOLDERS=$(find . -maxdepth 1 -type d -name "model.*");

for model_folder in $(find . -maxdepth 1 -type d -name "model.*" | sort -V);
do

   echo "entering to $model_folder";
   cd $model_folder;
   src_tgt=$(echo $model_folder | cut -d '.' -f4);
   #echo "source_target: $src_tgt";
   src=${src_tgt:0:-2};
   tgt=${src_tgt:2};
   echo "source: $src";
   echo "target: $tgt";
   for hypfile in $(find . -name "hyp.iter*.*" | sort -V);
   do
      # parallel data folder names are dw-bk and rk-bk and thus we need to check with if condition
      if [[ "$src" == "dw" || "$tgt" == "dw" ]]; 
      then 
         data_folder="dw-bk";
      else 
         data_folder="rk-bk";
      fi	      

      echo "ref: /home/ye/exp/pivot-nmt-baseline/data/word/$data_folder/1/test.$tgt";
      echo "hyp: $hypfile";
      python /home/ye/tool/chrF/chrF++.py -R /home/ye/exp/pivot-nmt-baseline/data/word/$data_folder/1/test.$tgt -H $hypfile;
   done
   cd ..;
   echo -e "==========\n";
	   

done

