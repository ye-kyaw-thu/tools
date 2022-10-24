#!/usr/bin/perl
use warnings;
use strict;

# for cleaning blank fields of Khmer Polarity Corpus
# Ye Kyaw Thu, Affiliate Professor, IDRI, CADT
# Last updated: 24 Oct 2022
#
# Preparation for 4th NLP/AI Workshop 2022
# e.g. $ perl ./check-empty-field.pl < ./kh-polar.shuf.clean > chk.out

my $line_no = 1;
while (<STDIN>) {
   my $line = $_;
   if (($line ne '') & ($line !~ /^ *$/)) {
      chomp($line);
      my $col1 = "<blank>"; my $col2 = "<blank>"; my $col3 = "<blank>";
      ($col1, $col2, $col3) = split (/\|\|\|/, $line);
      $col1 =~ s/^\s+|\s+$//g; $col2 =~ s/^\s+|\s+$//g; $col3 =~ s/^\s+|\s+$//g;
      $col1 =~ s/ +/ /g; $col2 =~ s/ +/ /g; $col3 =~ s/ +/ /g;
      if (length($col1) eq 0 || length($col2) eq 0 || length($col3) eq 0) {
         print("$line_no\t$col1 ||| $col2 ||| $col3\n");
      }
      $line_no = $line_no + 1;
   }
}
