#!/usr/bin/perl
use warnings;
use strict;
use utf8;

# for mypos data to json format conversion
# Written by Ye Kyaw Thu, LST, NECTEC, Thailand
# How to run:
# e.g. perl ./mypos2json.pl <input-file>
# perl ./mypos2json.pl ./mypos-dver.1.0.txt.clean > ./mypos.json

binmode STDIN,  ":utf8";
binmode STDOUT, ":utf8";
binmode(STDERR, ":utf8");

open (my $inputFILE,"<:encoding(utf8)", $ARGV[0]) or die "Couldn't open input file $ARGV[0]!, $!\n";
print("[\n");
   while(my $line = <$inputFILE>)
   {
      if ($line!~/^$/)
      {
         chomp ($line);
         $line =~ s/\|/ /g; # if your data not using pipe "|" comment out this line
         $line =~ s/\"/\\\"/g; # escaping double quote
         my @token = split('\s', $line);
         print("  [\n"); my $tmpStr="";
         foreach my $one_token(@token)
         {
            my($word, $POS) = split('\/', $one_token);
            $tmpStr=$tmpStr.",\n    [\"$word\"\,\"$POS\"]";
         }
         $tmpStr=~s/^,\n//; $tmpStr=$tmpStr."\n  ]";
         if (eof($inputFILE)) {
            print("$tmpStr\n");
         }else {
           print("$tmpStr,\n");
         }
      }
    }
print("]\n");

close($inputFILE);
