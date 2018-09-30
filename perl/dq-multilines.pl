#!/usr/bin/env perl

# Wroking on double quoted multilines
# Ye Kyaw Thu, Waseda University, Japan
#
# last updated: 30 Sept 2018 
# Used for cleaning facebook comments.
#
# usage: perl dq-multilines.pl <input-file> [options] 
# e.g. 1: perl dq-multilines.pl dq-tst -raw
# e.g. 2: perl dq-multilines.pl dq-tst -single
# e.g. 3: perl dq-multilines.pl dq-tst -remove

use strict;
use warnings;
use utf8;

binmode(STDIN, ":utf8");
binmode(STDOUT, ":utf8");
binmode(STDERR, ":utf8");

if (! defined $ARGV[1]){
   print "Usage: perl dq-multilines.pl <input-file> [-raw|-single|-remove]\n";
   exit 1;
}

open (my $inputFILE,"<:encoding(utf8)", $ARGV[0]) or die "Couldn't open input file $ARGV[0]!, $!\n";

my $data_of_whole_file = "";
$data_of_whole_file =  do { local $/; <$inputFILE> };

if (($ARGV[1] eq "-raw") || ($ARGV[1] eq "-single")){

   # checking double quoted multilines
   while ($data_of_whole_file =~ /("[^"]*(\\.[^"]*)*")/g) {

      if ($ARGV[1] eq "-raw"){

         print $1."\n";

      }elsif ($ARGV[1] eq "-single"){
         my $updatedLine = $1;
         chomp($updatedLine);
         $updatedLine =~ s/\n/ /g;

         print $updatedLine."\n";
      }  

   }

}elsif ($ARGV[1] eq "-remove"){

   $data_of_whole_file =~ s/"[^"]*(\\.[^"]*)*"//g;
      
   # removing blank lines
   # Here note that "^$" is not working and you also need "m"
   $data_of_whole_file =~ s/^\s*\n//mg;
   print $data_of_whole_file;

}

close ($inputFILE);

