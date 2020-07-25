#!/usr/bin/env perl

# read TAB separated input file line by line and print as latex file
# Ye Kyaw Thu, LST, NECTEC, Thailand
#
# Preparation for human evaluation on machine translation output
# Last updated: 26 July 2020
# How to run: $ perl human-mt-eval-form.pl <input-file> >> <output-file>
# e.g. cp ./human-eval-form.bak ./human-eval-form.tex 
#perl ./human-mt-eval-form.pl ./ref.pbsmt.google.yandex.shuf.100 >> ./human-eval-form.tex
# xelatex ./human-eval-form.tex
# evince ./human-eval-form.pdf

use strict;
use warnings;
use utf8;

binmode(STDIN, ":utf8");
binmode(STDOUT, ":utf8");
binmode(STDERR, ":utf8");

open (my $inputFILE,"<:encoding(utf8)", $ARGV[0]) or die "Couldn't open input file $ARGV[0]!, $!\n";

sub wrap_string{
    my $longstr = shift;        
    my @parts = $longstr =~ /(.{1,70})/g; # split string with length=70
        foreach (@parts) {
            print("\\padauktext{\\textbf {$_}}");
    }
}

my $lineno=1;
while (!eof($inputFILE)) {
     
    my $line = <$inputFILE>;
    if (($line ne '') & ($line !~ /^ *$/)) {

        print("\\begin{Form}\n");
        print("\\begin{tabbing}\n");
        print("xxxxxxxxxx: \\= \\kill  \n");

        chomp($line);
        my ($ref, $baseline, $google, $yandex) = split("\t", $line);
        if (length($ref) > 70) {
            print("\\textbf{Ref [$lineno]:} ");
            wrap_string("$ref");
            print("\\\\[1mm] \n");
        } else {
            print("\\textbf{Ref [$lineno]:} \\padauktext{\\textbf {$ref}} \\\\ \\\\ \n");
        }

        if (length($baseline) > 70) {
            print("\\noindent Hyp [1]: ");
            wrap_string("$baseline");
#            print("\\\\[1mm]"); 
        } else {
            print("\\noindent Hyp [1]: \\padauktext{$baseline}\\\\[1mm]"); 
        }
print(" \\hspace{5mm} \\textbf{Adequacy:} \\ChoiceMenu[combo,name=hyp1,charsize=11pt]{\\mbox{}}
{5 All,4 Most,3 Much,2 Little,1 None} \\hspace{3mm} \\textbf{Fluency:} \\\ChoiceMenu[combo,name=hyp1,charsize=11pt]{\\mbox{}}
{5 All,4 Most,3 Much,2 Little,1 None}\\\\[1mm]\n");
        print("%3mm vertical space\n");
#        print ("Hyp [2]: \\padauktext{$google} \\\\[1mm]");
        if (length($google) > 70) {
            print("Hyp [2]: ");
            wrap_string("$google");
  #          print("\\\\[1mm]"); 
        } else {
            print("Hyp [2]: \\padauktext{$google}\\\\[1mm]"); 
        }
        print("\\hspace{5mm} \\textbf{Adequacy:} \\ChoiceMenu[combo,name=hyp1,charsize=11pt]{\\mbox{}}
{5 All,4 Most,3 Much,2 Little,1 None} \\hspace{3mm} \\textbf{Fluency:} \\ChoiceMenu[combo,name=hyp1,charsize=11pt]{\\mbox{}}
{5 All,4 Most,3 Much,2 Little,1 None}\\\\[1mm]\n");
#        print ("\\noindent Hyp [3]: \\padauktext{$yandex} \\\\[1mm]");
        if (length($yandex) > 70) {
            print("Hyp [3]: ");
            wrap_string("$yandex");
  #          print("\\\\[1mm]"); 
        } else {
#            print("\\textbf{Ref [$lineno]:} \\padauktext{\\textbf {$ref}} \\\\ \\\\ \n");
            print("Hyp [3]: \\padauktext{$yandex}\\\\[1mm]"); 
        }
print("\\hspace{5mm} \\textbf{Adequacy:} \\ChoiceMenu[combo,name=hyp1,charsize=11pt]{\\mbox{}}
{5 All,4 Most,3 Much,2 Little,1 None} \\hspace{3mm} \\textbf{Fluency:} \\ChoiceMenu[combo,name=hyp1,charsize=11pt]{\\mbox{}}
{5 All,4 Most,3 Much,2 Little,1 None}\\\\[1mm]\n\n");
    print("\\end{tabbing}\n");
    print("\\end{Form}\n\n");

        $lineno++;
    }
}
print("\\end{document}\n\n");

close ($inputFILE);

