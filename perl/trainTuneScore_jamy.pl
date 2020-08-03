#!/usr/bin/perl -w
use strict;

# Perl Scripts for training, tuning and BLEU scoring with moses decoder (for running machines)
# Code by Ye Kyaw Thu, NICT
# Last updated: 22 Dec 2012
#
# Command for running:
#$perl trainTuneScore.pl > trainTuneScore-ar-en.log
# note: 2>&1 | tee is not s


###############################################################
# Variables Preparation for Japanese to Myanmar Translation Training
###############################################################

# home folder 
my $nictHome = "/panfs/panltg2/users/ye/";

# translation folder for Source Language to Target Language
my $pathSourceTarget = "ja-my/";
my $sourceExtension = "ja";
my $targetExtension = "my";

#/panfs/panltg2/users/ye/mt/corpus/forICCA2013/123/syl/
my  $pathTrain = $nictHome."mt/corpus/forICCA2013/123/syl/";

#my $pathTuneData = $nictHome."mt/corpus/forICCA2013/123/syl/"
# to update

# *** Note: currently, I put all data (i.e. training data, tune data and test data) under 
#~/mt/corpus/forICCA2013/123/syl/

#path of moses decoder
my $pathMosesTraining = $nictHome."mt/moses-0.91/scripts/training/";
my $pathMosesBin = $nictHome."mt/moses-0.91/bin/";
my $pathMosesScripts = $nictHome."mt/moses-0.91/scripts/";

#path of IRSTLM
my $pathIRSTLM = $nictHome."mt/irstlm-5.80.01/bin/";

#bin folder
my $pathGIZABin = $nictHome."mt/giza-pp/bin/";

#source language test sentences
my $strTargetLanguage1 = "ဒီ က နေ ဟို တယ် အ ခန်း ကို ဘွတ် ကင် တင် ပေး ပါ လား ။ ";
my $strTargetLanguage2 = "ဘိန်း မုန့် ကို ပေး ပါ ။ ";
my $strTargetLanguage3 = "ကူ ညီ ခဲ့ တဲ့ အ တွက် ကျေး ဇူး တင် ပါ တယ် ။ ";
my $strTargetLanguage4 = "လျှော့ ဈေး နဲ့ ရောင်း တဲ့ လက် မှတ် တွေ ကို ဘယ် မှာ ဝယ် လို့ ရ မ လဲ ။ ";
my $strTargetLanguage5 = "ဆိုဒ် နှစ် သို့ မ ဟုတ်  လေး ဖြစ် နိုင် တယ် ။ ";
my $strTargetLanguage6 = "ဘတ်စ် ကား ကို ဆောင် ရွက် ပေး ပါ ။ ";
my $strTargetLanguage7 = "ဟုတ် ကဲ့ ။ ဒါ ပေ မဲ့ ၊ ကျေး ဇူး ပြု ပြီး ၊ ဖ လက် ရှ် မ ဖွင့် ပါ နဲ့ ။ ";
my $strTargetLanguage8 = "ဒီ မှာ  ဒေါ် လာ တစ် ရာ တန် ပါ ။ ";
my $strTargetLanguage9 = "၅ ၀ ဆင့် အ ကြွ စေ့ ကို ၂ ၀ စေ့ နဲ့ ၁ ဒေါ် လာ တန် ကို ၁ ၀ ရွက် ၊ ၁ ၀ ဒေါ် လာ တန် ကို ၅ ရွက် လုပ် ပေး ပါ ။ ";
my $strTargetLanguage10 = "ကျ နော့် ရဲ့ ဟော် တယ် က သော့ ကို အ ခိုး ခံ လိုက် ရ ပါ တယ် ။ ";


#target language test sentences
my $strSourceLanguage1 = "おはよう 。";
my $strSourceLanguage2 = "こんばんは 。";
my $strSourceLanguage3 = "おやすみなさい 。";
my $strSourceLanguage4 = "さようなら 。";
my $strSourceLanguage5 = "では また 。";
my $strSourceLanguage6 = "ご き げん いかが です か 。";
my $strSourceLanguage7 = "元気 です 、 ありがとう 。";
my $strSourceLanguage8 = "まあまあ です 。";
my $strSourceLanguage9 = "大丈夫 です か 。";
my $strSourceLanguage10 = "大丈夫 です 。";

###########################
# Data preparation for training
############################

print("\n### Start data preparation for training ...\n\n");

#$pathTrain=/panfs/panltg2/users/ye/mt/corpus/forICCA2013/123/syl/"
chdir($pathTrain);

#system("mkdir -p my-ja");
system("mkdir -p ".$pathSourceTarget);

#chdir("my-ja");
chdir($pathSourceTarget);
#pwd is /panfs/panltg2/users/ye/mt/corpus/forICCA2013/123/my-ja/

system("echo \"pwd:\"; pwd");

#system("cp ~/mt/corpus/forICCA2013/123/123*.my .");
system("cp ".$pathTrain."123*.$sourceExtension .");
system("cp ".$pathTrain."123*.$targetExtension .");

#system("~/mt/moses-0.91/scripts/training/clean-corpus-n.perl ./123train.tkn my ja ./123train.tkn.my-ja.clean 1 80");
system($pathMosesTraining."clean-corpus-n.perl ./123train.tkn ".$sourceExtension." ".$targetExtension." ./123train.tkn.".$sourceExtension."-".$targetExtension.".clean 1 100");

#print("\n### Output of command: wc  -l 123train.tkn.my-ja.clean.*\n");
print("\n### Output of command: wc  -l 123train.tkn.".$sourceExtension."-".$targetExtension.".clean.*\n\n");
#system("wc -l 123train.tkn.my-ja.clean.*");
system("wc -l 123train.tkn.".$sourceExtension."-".$targetExtension.".clean.*");

#Adding Start and End Tag
print("\n### Adding start and end tag ...\n\n");
#system("~/mt/irstlm-5.80.01/bin/add-start-end.sh < ./123train.tkn.my-ja.clean.my > 123train.tkn.my-ja.sb.my");
system($pathIRSTLM."add-start-end.sh < ./123train.tkn.".$sourceExtension."-".$targetExtension.".clean.".$targetExtension." > 123train.tkn.".$sourceExtension."-".$targetExtension.".sb.".$targetExtension);

#print("\n### Output of command: head 123train.tkn.my-ja.sb.ja\n");
print("\n### Output of command: head 123train.tkn.".$sourceExtension."-".$targetExtension.".sb.".$targetExtension."\n\n");
#system("head 123train.tkn.my-ja.sb.ja");
system("head 123train.tkn.".$sourceExtension."-".$targetExtension.".sb.".$targetExtension);

#########################
# Language Model Building
#########################

print("\n### Start language model building with IRSTLM ...\n\n");
#system("~/mt/irstlm-5.80.01/bin/build-lm.sh -i 123train.tkn.my-ja.sb.ja -t ./tmp -p -s improved-kneser-ney -o 123train.tkn.my-ja.lm.ja");
system($pathIRSTLM."build-lm.sh -i 123train.tkn.".$sourceExtension."-".$targetExtension.".sb.".$targetExtension." -t ./tmp -p -s improved-kneser-ney -o 123train.tkn.".$sourceExtension."-".$targetExtension.".lm.".$targetExtension);

#Compile to get arpa file
print("\n### Start compile to get arpa file ...\n\n");
#system("~/mt/irstlm-5.80.01/bin/compile-lm --text yes 123train.tkn.my-ja.lm.ja.gz 123train.tkn.my-ja.arpa.ja");
system($pathIRSTLM."compile-lm --text yes 123train.tkn.".$sourceExtension."-".$targetExtension.".lm.".$targetExtension.".gz 123train.tkn.".$sourceExtension."-".$targetExtension.".arpa.".$targetExtension);

#Build binary file (i.e. blm file)
print("\n### Build binary file ...\n\n");
#system("~/mt/moses-0.91/bin/build_binary ./123train.tkn.my-ja.arpa.ja ./123train.tkn.my-ja.blm.ja");
system($pathMosesBin."build_binary ./123train.tkn.".$sourceExtension."-".$targetExtension.".arpa.".$targetExtension." ./123train.tkn.".$sourceExtension."-".$targetExtension.".blm.".$targetExtension);

#########################
# Testing language model
#########################

print("\n### Testing language model ...\n\n");
#system("echo \"早上 好 。\" | ~/mt/moses-0.91/bin/query ./123train.tkn.my-ja.blm.ja ");
#system("echo \"早上 好 。\" | ".$pathMosesBin."query ./123train.tkn.my-ja.blm.ja ");

system("echo \"".$strTargetLanguage1."\" | ".$pathMosesBin."query ./123train.tkn.".$sourceExtension."-".$targetExtension.".blm.".$targetExtension);
system("echo \"".$strTargetLanguage2."\" | ".$pathMosesBin."query ./123train.tkn.".$sourceExtension."-".$targetExtension.".blm.".$targetExtension);
system("echo \"".$strTargetLanguage3."\" | ".$pathMosesBin."query ./123train.tkn.".$sourceExtension."-".$targetExtension.".blm.".$targetExtension);
system("echo \"".$strTargetLanguage4."\" | ".$pathMosesBin."query ./123train.tkn.".$sourceExtension."-".$targetExtension.".blm.".$targetExtension);
system("echo \"".$strTargetLanguage5."\" | ".$pathMosesBin."query ./123train.tkn.".$sourceExtension."-".$targetExtension.".blm.".$targetExtension);
system("echo \"".$strTargetLanguage6."\" | ".$pathMosesBin."query ./123train.tkn.".$sourceExtension."-".$targetExtension.".blm.".$targetExtension);
system("echo \"".$strTargetLanguage7."\" | ".$pathMosesBin."query ./123train.tkn.".$sourceExtension."-".$targetExtension.".blm.".$targetExtension);
system("echo \"".$strTargetLanguage8."\" | ".$pathMosesBin."query ./123train.tkn.".$sourceExtension."-".$targetExtension.".blm.".$targetExtension);
system("echo \"".$strTargetLanguage9."\" | ".$pathMosesBin."query ./123train.tkn.".$sourceExtension."-".$targetExtension.".blm.".$targetExtension);
system("echo \"".$strTargetLanguage10."\" | ".$pathMosesBin."query ./123train.tkn.".$sourceExtension."-".$targetExtension.".blm.".$targetExtension);

# ###############################
# Start training with moses decoder
# ###############################

system("mkdir -p working");
chdir("working");
system("echo \"pwd:\"; pwd");

print("\n### Start training with moses decoder ...\n\n");
#system("nohup nice ~/mt/moses-0.91/scripts/training/train-model.perl -external-bin-dir ~/mt/giza-pp/bin/ -root-dir train -corpus ~/mt/corpus/forICCA2013/123/my-ja/123train.tkn.my-ja.clean -f my -e ja -alignment grow-diag-final-and -reordering msd-bidirectional-fe -lm 0:3:~/mt/corpus/forICCA2013/123/my-ja/123train.tkn.my-ja.blm.ja:8 2>&1 | tee training.out &");

# I removed "&" at end of above "nohup nice xxxx ... " command line
system("nohup nice ".$pathMosesTraining."train-model.perl -external-bin-dir ".$pathGIZABin." -root-dir train -corpus ".$pathTrain.$pathSourceTarget."123train.tkn.".$sourceExtension."-".$targetExtension.".clean -f ".$sourceExtension." -e ".$targetExtension." -alignment grow-diag-final-and -reordering msd-bidirectional-fe -lm 0:3:".$pathTrain.$pathSourceTarget."123train.tkn.".$sourceExtension."-".$targetExtension.".blm.".$targetExtension.":8 2>&1 | tee training.out ");

print ("\n###  !!!!! Training finished !!!!! \n\n");

# perl -e 'system("charmap &"); print "yes";' 

#########################
# Test translation engine
########################

chdir("train/model/");
system("echo \"pwd:\"; pwd");
print ("\n### Let's test translation engine for ".$sourceExtension." to ".$targetExtension." ...\n\n");
print "### moses decoder will start from now on ...\n\n";
print ("### Don't forget to prepare some ".$sourceExtension." sentences in advance for testing ...\n\n");
system("~/mt/moses-0.91/bin/moses -f ./moses.ini");

#################################
# Data preparation for tuning process
#################################

# Preparation for source language mref file:
# --------------------------------
# /media/HDPC-U/backup/BTEC/BTEC1/test/TKN_120131/ja$ cp jpn_set01.mref.ja.TKN.1 ~/mt/corpus/BTEC1/test/ja
# cd ~/mt/corpus/BTEC1/test/ja
# ~/mt/corpus/BTEC1/test/ja$ head jpn_set01.mref.ja.TKN.1 
# ~/mt/corpus/BTEC1/test/ja$ cut -d '\' -f 8- jpn_set01.mref.ja.TKN.1 > jpn_set01.mref.ja.TKN_Cut.1 
# ~/mt/corpus/BTEC1/test/ja$ head jpn_set01.mref.ja.TKN_Cut.1 
# ~/mt/corpus/BTEC1/test/ja$ wc *

chdir($pathTrain);
#chdir($pathTrain.$pathSourceTarget);
chdir($pathSourceTarget);
system("### echo \"pwd:\"; pwd");
# 123dev.tkn.en
# 
print("\n### Output of command: head 123dev.tkn.".$sourceExtension."\n\n");
system("head ./123dev.tkn.".$sourceExtension);

##################################################################################################
# Preparation for target language mref file: (just putting for reference!)
# ------------------------------------
# mkdir ~/mt/corpus/BTEC1/test/zh
# cd /media/HDPC-U/backup/BTEC/BTEC1/test/TKN_120131/zh
# cp jpn_set01.mref.zh.TKN.1 ~/mt/corpus/BTEC1/test/zh
# cd ~/mt/corpus/BTEC1/test/zh
# ~/mt/corpus/BTEC1/test/zh$ head jpn_set01.mref.zh.TKN.1 
# ~/mt/corpus/BTEC1/test/zh$ cut -d '\' -f 8- jpn_set01.mref.zh.TKN.1 > jpn_set01.mref.zh.TKN_Cut.1 
# ~/mt/corpus/BTEC1/test/zh$ head jpn_set01.mref.zh.TKN_Cut.1 
# ~/mt/corpus/BTEC1/test/zh$ wc *
###################################################################################################

print("\n### Output of command: head 123dev.tkn.".$targetExtension."\n\n");
system("head ./123dev.tkn.".$targetExtension);
system("wc ./123dev.tkn.*");

# Cleaning Data for tuning process

print("\n### Run clean-corpus-n.perl for \"123dev.tkn.".$sourceExtension."\" and \"123dev.tkn.".$targetExtension."\" \n\n");
#$/panfs/panltg2/users/ye/mt/moses-0.91/scripts/training/clean-corpus-n.perl ./123dev.tkn my ja ./123dev.tkn.my-ja.clean 1 100
system($pathMosesTraining."clean-corpus-n.perl ./123dev.tkn ".$sourceExtension." ".$targetExtension." ./123dev.tkn.".$sourceExtension."-".$targetExtension.".clean 1 100");

#system("ls ".$pathTrain."/123dev.tkn.*");
system("ls ./123dev.tkn.*");
#system("wc -l 123dev.tkn.my-ja.clean.*");
system("wc -l 123dev.tkn.".$sourceExtension."-".$targetExtension.".clean.*");

########################
# Start tuning process
########################

system("echo \"pwd:\"; pwd");
chdir($pathTrain.$pathSourceTarget."working");
system("echo \"pwd:\"; pwd");
#pwd=/panfs/panltg2/users/ye/mt/corpus/forICCA2013/123/syl
# Don't forget to prepare clean mref data file before running tuning process

#nohup nice ~/mt/moses-0.91/scripts/training/mert-moses.pl ~/mt/corpus/forICCA2013/123/syl/123dev.tkn.my-ja.clean.my ~/mt/corpus/forICCA2013/123/syl/123dev.tkn.my-ja.clean.ja ~/mt/moses-0.91/bin/moses ~/mt/corpus/forICCA2013/123/syl/my-ja/train/model/moses.ini --mertdir ~/mt/moses-0.91/bin/ &> mert.out &

print("\n### Start tuning process ...\n\n");
system("nohup nice ".$pathMosesTraining."mert-moses.pl ".$pathTrain.$pathSourceTarget."123dev.tkn.".$sourceExtension."-".$targetExtension.".clean.".$sourceExtension." ".$pathTrain.$pathSourceTarget."123dev.tkn.".$sourceExtension."-".$targetExtension.".clean.".$targetExtension." ".$pathMosesBin."moses ".$pathTrain.$pathSourceTarget."working/train/model/moses.ini --mertdir ".$pathMosesBin." 2>&1 | tee mert.out");


##############################################
# test translation with "mert-work/moses.ini"
##############################################

#$ ~/mt/moses-0.91/bin/moses -f ~/mt/corpus/forICCA2013/123/my-ja/train/model/mert-work/moses.ini

print("\n### Run moses decoder with /working/mert-work/moses.ini \n\n");
#system($pathMosesBin."moses -f ".$pathTrain.$pathSourceTarget."working/mert-work/moses.ini");
system($pathMosesBin."moses -f ./mert-work/moses.ini");

# prepare some test phrases for this stage!
# パスポート を なく し て しまい まし た 。
# まあ 、 たいへん 。
# やめ て 。
# 一 二 三 、 八 七 六 五 です 。
# これ を 新しい もの と 取り替え て いただけ ます か 。

########################################################
# Test Data Preparation (or) preparation for BLEU Score
########################################################

system("echo \"pwd:\"; pwd");
chdir($pathTrain);
system("echo \"pwd:\"; pwd");
#pwd=/panfs/panltg2/users/ye/mt/corpus/forICCA2013/123/syl/"

######################################
# Trained with FILTERED for test data set
######################################

system("echo \"pwd:\"; pwd");
chdir($pathTrain.$pathSourceTarget."working");
system("echo \"Moved to new path.\n pwd:\"; pwd");
#pwd=/panfs/panltg2/users/ye/mt/corpus/forICCA2013/123/syl/my-ja/"

# ~/mt/moses-0.91/scripts/training/filter-model-given-input.pl filtered-123testEn ./mert-work/moses.ini ~/mt/corpus/forICCA2013/123/syl/123test.tkn. -Binarizer ~/mt/moses-0.91/bin/processPhraseTable

print("\n### Trained with FILTERED for test data set \n\n");
system($pathMosesTraining."filter-model-given-input.pl filtered-123testEn ./mert-work/moses.ini ".$pathTrain."123test.tkn.".$sourceExtension." -Binarizer ".$pathMosesBin."processPhraseTable");

#############################################################
# Test moses decoder with test data set (i.e. 123test.tkn.my)
#############################################################

# nohup nice ~/mt/moses-0.91/bin/moses -f ~/mt/corpus/forICCA2013/123/syl/my-ja/train/model/filtered-123testEn/moses.ini < ~/mt/corpus/forICCA2013/123/syl/123test.tkn.my > ~/mt/corpus/forICCA2013/123/syl/my-ja/working/123test.translated.ja 2> ~/mt/corpus/forICCA2013/123/syl/my-ja/working/123test.tkn.test.my-ja.log &

print("\n### Test moses decoder with test data set (i.e. 123test.tkn.".$sourceExtension.") \n\n");
system("nohup nice ".$pathMosesBin."moses -f ".$pathTrain.$pathSourceTarget."working/filtered-123testEn/moses.ini < ".$pathTrain."123test.tkn.".$sourceExtension." > ".$pathTrain.$pathSourceTarget."working/123test.translated.".$targetExtension." 2> ".$pathTrain.$pathSourceTarget."working/123test.tkn.test.my-ja.log ");

##############################
# Evaluation with BLEU Score ...
##############################

# ~/mt/moses-0.91/scripts/generic/multi-bleu.perl -lc  ~/mt/corpus/forICCA2013/123/syl/123test.tkn.ja < ~/mt/corpus/forICCA2013/123/syl/my-ja/working/123test.translated.ja 

print("\n### Start evaluation with BLEU Score ...\n\n");
system($pathMosesScripts."generic/multi-bleu.perl -lc ".$pathTrain."123test.tkn.".$targetExtension." < ".$pathTrain.$pathSourceTarget."working/123test.translated.".$targetExtension);

# ======================== End Of Script ===================================

