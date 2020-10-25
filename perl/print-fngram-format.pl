#!/usr/bin/perl
use warnings;
use strict;
use utf8;

# last updated: 10 June 2017
# written by Ye Kyaw Thu, AI Lab.,
# Okayama Prefectural University, Japan
# How to run:
# e.g. perl ./print-fngram-format.pl ./mypos-dver.1.0.txt > mypos.fngram-format

binmode(STDIN, ":utf8");
binmode(STDOUT, ":utf8");
binmode(STDERR, ":utf8");

open (my $inputFILE,"<:encoding(utf8)", $ARGV[0]) or die "Couldn't open input file $ARGV[0]!, $!\n";
my $one_token; my $tmpLine="";

   while(my $line = <$inputFILE>)
   {
      if ($line!~/^$/)
      {
         chomp ($line);
         my $originalLine = $line;
            
         $line =~ s/\s+/ /g;
         $line =~ s/^\s+|\s+$//g;
         $line =~ s/\|/ /g;

         my @token = split('\s', $line);
         #print "\@tokens:\n"."@token\n"; 
            foreach $one_token(@token)
            {
            my ($text, $tag) = split(/\//, $one_token);
               $tmpLine = $tmpLine."W-".$text.":P-".$tag." ";
            }
               $tmpLine =~ s/^\s+|\s+$//g;
               $tmpLine =~ s/\s+/ /g;
               print("$tmpLine\n");  
         }   $tmpLine = "";
      }

close($inputFILE);
