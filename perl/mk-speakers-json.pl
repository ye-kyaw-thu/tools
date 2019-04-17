#!/usr/bin/env perl

# retrieving speaker information from path and filename and output as JSON
# Written by Ye Kyaw Thu, Visiting Professor,
# Language and Semantic Technology Research Team (LST), NECTEC, Thailand
#
# How to run: perl ./mk-speakers-json.pl <input-file>
# e.g. perl ./mk-speakers-json.pl ./100-wave-filenames2.txt > speakers-info.json
 
use strict;
use warnings;
use utf8;
use Data::Dumper;
use JSON;

binmode(STDIN, ":utf8");
binmode(STDOUT, ":utf8");
binmode(STDERR, ":utf8");

open (my $inputFILE,"<:encoding(utf8)", $ARGV[0]) or die "Couldn't open input file $ARGV[0]!, $!\n";

# hash for saving uniq speaker ID
my %spk_id;
 
   while (!eof($inputFILE)) {

      my $line = <$inputFILE>;

      # input format: /Spk1/Univ1-HninHnin-F-25-burmese-2637.wav
      #  splitting folder (i.e. speaker ID) and filename
      my @fields = split("\/", $line);
      
      # Although I can use $fields array directly, I used 2 variables for easy to understand
      my $speaker_ID = $fields[1];
      my $filename = $fields[2];

      #Univ1-AungAung-M-20-burmese-1025.wav
      my ($organization, $name, $gender, $age, $native_language, $line_no) = split ("-", $filename);
      $organization =~ s/\///;
      $line_no =~ s/\.wav//;
      chomp($line_no);

   #if not exist in the hash put the speaker id into hash
   if (exists $spk_id{$speaker_ID}) {

      # actually, this hash is just dummy for checking speaker ID already exist or not
      $spk_id{$speaker_ID}{"recorded_sentence"} = $spk_id{$speaker_ID}{"recorded_sentence"}.",".$line_no;

   } else {

      $spk_id{$speaker_ID}{"name"} = $name;
      $spk_id{$speaker_ID}{"organization"} = $organization;
      $spk_id{$speaker_ID}{"gender"} = $gender;
      $spk_id{$speaker_ID}{"age"} = $age;
      $spk_id{$speaker_ID}{"native_language"} = $native_language;
      $spk_id{$speaker_ID}{"recorded_sentence"} = $line_no;

   }

}
close ($inputFILE);

#print Dumper (%spk_id); 

# Redefine Data::Dumper::qquote() to do nothing
no warnings 'redefine';
local *Data::Dumper::qquote = sub { qq["${\(shift)}"] };
# Use the Pure Perl implementation of Dumper
local $Data::Dumper::Useperl = 1;

# converting hash into json format (for source)
my $spk_json = JSON->new->utf8(0)->encode(\%spk_id);
print $spk_json;

