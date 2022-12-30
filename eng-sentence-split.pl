#!/usr/bin/env perl

# English sentence splitting program with Lingua::EN::Sentence Perl Module
# Ye Kyaw Thu, 
# Visiting Professor, LST, NECTEC, Thailand
# Ref: https://www.perl.com/article/21/2013/4/21/Read-an-entire-file-into-a-string/
#
# Demo program for my undergrad student Thura Aung.
# e.g. $ perl eng-sentence-split.pl <input-file>
# (base) ye@ykt-pro:~/tmp$ perl ./eng-sentence-split.pl ./abstract-draft.txt | cat -n
#
# https://github.com/ye-kyaw-thu/error-overflow/blob/master/en-cpan-sentence-segmentation.md

use Lingua::EN::Sentence qw( get_sentences add_acronyms );
add_acronyms('lt','gen');               ## adding support for 'Lt. Gen.'

use strict;
use warnings;
use utf8;

binmode(STDIN, ":utf8");
binmode(STDOUT, ":utf8");
binmode(STDERR, ":utf8");

open (my $inputFILE,"<:encoding(utf8)", $ARGV[0]) or die "Couldn't open input file $ARGV[0]!, $!\n";

# Slurping: read an entire file into a string
my $file_content = do { local $/; <$inputFILE> };
close ($inputFILE);
 
my $sentences=get_sentences($file_content);     # Get the sentences.
foreach my $sent (@$sentences)
{
        print("$sent\n");
}

