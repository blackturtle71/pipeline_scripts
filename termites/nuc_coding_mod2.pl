#!/usr/bin/perl -w

%hash=();
@keys=();
open (I, "$ARGV[0]");
while(<I>)
{
push @I, $_;
if ($_=~/^RN_\d+|^OUTGRP/) {chomp; push @keys, $_}
}
close I;
chomp @I;
%hash=@I;

$NUC_FILE="";
foreach $key (@keys)
{
print STDERR "$hash{$key}\r";
@columns=split(/\s+/, $hash{$key});
$entry=$columns[0];
$range=$columns[$#columns];
$range=~s/:/-/;
$strand=$columns[$#columns-2];
$strand=~s/\+/plus/;
$strand=~s/\-/minus/;
$NUC_FILE.=">$key\n";
open (BLAST, "~/bin/blastdbcmd -db $ARGV[1] -entry $entry -range $range -strand 'plus' |");
while (<BLAST>)
{
unless ($_=~/^>/)
    {
    $NUC_FILE.=$_;
    }
}
close BLAST;
}

print "$NUC_FILE";
 
