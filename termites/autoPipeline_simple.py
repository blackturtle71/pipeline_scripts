

from Bio import SeqIO
import sys
import re
import subprocess

def to_dict_remove_dups (sequences):
	return {record.id: record.seq for record in sequences} 

file_name = sys.argv[1] #this is RefSeq CDS (genes) file containing one gene type, for example filtered (by gene names considering synonyms) GenesRefSeqs.fasta file
gene_name = sys.argv[2] #this is gene name

Sequences = to_dict_remove_dups(SeqIO.parse("newdb/cuts_nondb.fasta", "fasta"))

for Seq in Sequences:
        species_name = Seq
        value = Sequences[Seq]
	
        with open('nuc_seq.fa', 'w+') as nucl:
                nucl.write('>{0}\n{1}\n'.format(species_name,value))

        subprocess.call("~/bin/emboss/bin/transeq -sequence nuc_seq.fa -outseq prot_seq.pep -frame 1 -table 5", shell=True)

        prot = open ("prot_seq.pep", "r")
        lines = prot.readlines()
        prot.close()
        protein = "".join(map(str.strip, lines[1:]))
        
        subprocess.call('./SCRIPT2.2.1.sh %s %s %s' % (species_name, protein, gene_name), shell=True)
 
