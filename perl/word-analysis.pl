#!/usr/bin/perl
use strict;
use warnings;
use utf8;

# Last updated: 23 Oct 2016
# For anlysis of number of words
# Written by Ye Kyaw Thu, Okayama Prefectural University, Japan

# Note:
# input file already finished word breaking
# How to run: word-analysis.pl <input-filename> [options]
# e.g.
# word-analysis.pl 10-lines
# word-analysis.pl 10-lines longest-shortest
# word-analysis.pl 10-lines count 

binmode STDIN, ":utf8";
binmode STDOUT, ":utf8";
 
open (iFILE, "<:encoding(UTF-8)", $ARGV[0]) or die "Couldn't open input file $ARGV[0]!, $!\n";
#open (iFILE, $ARGV[0]) or die "Couldn't open input file $ARGV[0]!, $!\n";

my $line;my %word;my %sent;
my $word_per_sentence; my $line_no =0;

while ($line = <iFILE>)
{
    chomp($line);
    $word_per_sentence =0;
    $line_no = $line_no +1;
    #$line =~ s/၊|။//g; #rm pot htee & pot ma
    ++$word_per_sentence while $line =~ /\S+/g;
    $word{$line_no}=$word_per_sentence;
    
    if(exists $sent{$word_per_sentence})
    {
        $sent{$word_per_sentence}=$sent{$word_per_sentence}.",".$line_no." : ".$line;
    }else
    {
        $sent{$word_per_sentence}=$line_no." : ".$line;
    }
}
close(iFILE);

my $total_no_words = 0;
my $total_no_sentences  = keys %word;

foreach (sort { $a <=> $b } keys (%word))
{
    #print  "line no. $_: $word{$_}\n";
    $total_no_words = $total_no_words + $word{$_};
}

if (! defined $ARGV[1])
{

    foreach my $key ( sort {$a <=> $b} keys %sent )
    {
        print "$key word(s) sentence(s) : \n";
        my $current_sent = $sent{$key};
        my $count = ($current_sent =~ s/,/\n\t/g);
        $count = $count+1;
        print "\t$current_sent\n";
        print "total: $count\n\n";
    }
        
    printf ("Average words per line : %.2f\n", $total_no_words/$total_no_sentences);
}
elsif ($ARGV[1] eq "longest-shortest")
{
    my $highest_val; my $count=0;
    $highest_val = (reverse sort {$word{$a} <=> $word{$b}} keys %word)[0];
    print "Longest sentence : $word{$highest_val} words\n";

    my $ls = $sent{$word{$highest_val}};
    $count = ($ls =~ s/,/\n\t/g); $count = $count+1;
    print "\t$ls\n";
    print "total : $count\n\n";
    
    my $lowest_val = (sort {$word{$a} <=> $word{$b}} keys %word)[0];
    
    if ($word{$highest_val} != $word{$lowest_val})
    {
        print "\nShortest sentence : $word{$lowest_val} word(s)\n";

        my $ss = $sent{$word{$lowest_val}};
        $count = ($ss =~ s/,/\n\t/g); $count = $count+1;
        print "\t$ss\n";
        print "total : $count\n\n";
    
        printf ("Average words per line : %.2f\n", $total_no_words/$total_no_sentences);
     }else
     {
         print "*** All sentences have same number of words!\n";
     }
}
elsif ($ARGV[1] eq "count")
{
    foreach my $key ( sort {$a <=> $b} keys %sent )
    {
        print "$key word(s) : ";
        my $current_sent = $sent{$key};
        my $count = ($current_sent =~ s/,/\n\t/g);
        $count = $count+1;
        #print "\t$current_sent\n";
        print "$count sentence(s)\n";
    }
        
    printf ("Average words per line : %.2f\n", $total_no_words/$total_no_sentences);

}
