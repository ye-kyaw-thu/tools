use strict;
use warnings;
use utf8;

# for removing lines that contained only one character
# written by Ye Kyaw Thu,
# Language Semantic Technology Research Team (LST), NECTEC, Thailand
# how to run: perl ./rm-onechar-line.pl <filename>
# e.g. perl ./rm-onechar-line.pl ./bookmar.zh-my.f2.nospace.syl.line > out

binmode STDIN, ":encoding(UTF-8)";
binmode STDOUT, ":encoding(UTF-8)";

open (my $sylFILE,"<:encoding(utf8)", $ARGV[0]) or die "Couldn't open input file $ARGV[0]!, $!\n";

while( my $line = <$sylFILE>)  {

   chomp($line);
   my $lenLine = length($line);
   if ($lenLine > 1) {
      print ("$line\n");
   }
}

close($sylFILE);

