#!/usr/bin/perl

use lib './';
use sylbreak;
#require sylbreak;

use strict;
use warnings;
use utf8;
binmode STDIN, ":encoding(UTF-8)";
binmode STDOUT, ":encoding(UTF-8)";

while (my $line = <STDIN>)
{
   print (sylbreak::syllable("$line", "_"), "\n");
   print (sylbreak::syllableWord("$line", "_"), "\n");
}
