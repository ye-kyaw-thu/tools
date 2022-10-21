#!/usr/bin/perl -w
use warnings;
use strict;
use utf8;

# Spelling dictionary building demo code for ICT internship students
# Written by Ye Kyaw Thu, IDRI, CADT, Cambodia
# Last updated: 21 Oct 2022
# Input file format is as follows:
# បើ<គាត>ការពារព្រៃឈើមិនបាន គាត់នឹងកាត់ក្បាលគាត់ចោល ||| បើ(គាត់/vow)ការពារព្រៃឈើមិនបាន គាត់នឹងកាត់ក្បាលគាត់ចោល
# សាកធ្វើតាមបងហើយរសជាតិឆ្ងាញ់ថែមអំពិល<ទំ>បន្តិច|||សាកធ្វើតាមបងហើយរសជាតិឆ្ងាញ់ថែមអំពិល(ទុំ/pho)បន្តិច
# សុំប្អូនជួយថតស្ពានស្រែង<អោយ>បងប្អូនយើងមើលផង|||សុំប្អូនជួយថតស្ពានស្រែង(ឲ្យ/dia)បងប្អូនយើងមើលផង
# How to run:
# e.g. perl ./mk-spelling-dict.pl <input-file> [text|type]
# Here, text = text only and type = text/type format
# $ perl ./mk-spelling-dict.pl ./input.txt text > out

binmode(STDIN,  ":utf8");
binmode(STDOUT, ":utf8");
binmode(STDERR, ":utf8");

# option for print out only text or with type
my $text_or_type = $ARGV[1];

open (my $inputFILE,"<:encoding(utf8)", $ARGV[0]) or die "Couldn't open input file $ARGV[0]!, $!\n";

   while(my $line = <$inputFILE>)
   {
      if ($line!~/^$/)
      {
         chomp ($line);
         my($error, $correction) = split('\|\|\|', $line);
         #print("Spelling Mistake: $error\n");
         #print("Correction: $correction\n"); exit();

         # "<" and ">" are meta characters and needs to be escaped if you want to match it literally and thus I used >         # (.*?) match any characters in a non-greedy way and then capture it
         # g for global matching
         my @error_word =($error=~/\<(.*?)\>/g);
         #print ("@error_word\n");

         # "(" and ")" are meta characters and needs to be escaped if you want to match it literally and thus I used >         my @correct_word=($correction=~/\((.*?)\)/g);
         #print ("@correct_word\n");         

         # $#Array_Name is predefined variable for getting the length of an array
         if ($#error_word != $#correct_word) {
            print("Error! Array lengths are different in line no. $.!\n");
         } else {
                for my $i (0 .. $#correct_word) {
                   #split "correct word" and "error class type"
                   my($correct_text, $type) = split('\/', $correct_word[$i]);
                   if ($text_or_type eq "type") {
                      print("$error_word[$i]\t$correct_text\t$type\n");
                   } elsif ($text_or_type eq "text") {
                      print("$error_word[$i]\t$correct_text\n");

                   }
               }
            }
         }
   }

close($inputFILE);

