#!/bin/bash
#PBS -q eternity ## big eternity mem1t mem512g
#PBS -d .
#PBS -l walltime=300:00:00,mem=10G,nodes=1:ppn=4

#SPNAME='taxon:36984';
#GENE='COX2'

module load python/python-3.8.2

#python3 /home/agmikhaylova/termites/autoPipeline_simple.py /home/agmikhaylova/termites/newdb/COX2taxid.fasta COX2 > /mnt/lustre/agmikhaylova/termites/result.out

#~/bin/tblastn -db ~/termites/newdb/cut_nucls.fasta -db_gencode 5 -num_alignments 500 -query ~/termites/newdb/prot_seq.pep -out query.out-mitocode 1>~/termites/tblastn.log 2>~/termites/tblastn.err

#/mnt/lustre/genkvg/perl5/perlbrew/perls/perl-5.28.1/bin/perl ~/bin/mview -in blast -out fasta query.out-mitocode 1>query.out-mitocode.fa 2>/dev/null

#/mnt/lustre/genkvg/perl5/perlbrew/perls/perl-5.28.1/bin/perl ~/bin/header_sel_mod3.pl query.out-mitocode.fa $SPNAME 1>query.out-mitocode_sel.fa 2>query.out-mitocode_sel.hash

#/mnt/lustre/genkvg/perl5/perlbrew/perls/perl-5.28.1/bin/perl ~/termites/nuc_coding_mod2.pl query.out-mitocode_sel.hash ~/termites/newdb/cut_nucls.fasta 1>query.out-mitocode_sel.nuc 2>~/termites/query_sel_nuc_err

#/mnt/lustre/genkvg/perl5/perlbrew/perls/perl-5.28.1/bin/perl ~/bin/codon_alig_unique.pl query.out-mitocode_sel.nuc 1>query.out-mitocode_sel_unique.fa 2>~/termites/codon_alig_unique.log

#java -jar ~/bin/macse_v1.01b.jar -prog alignSequences -gc_def 5 -out_AA query.out-mitocode_sel_protalign_unique.fa -out_NT query.out-mitocode_sel_tranalign_unique.fa -seq query.out-mitocode_sel_unique.fa

#~/bin/macse2.pl query.out-mitocode_sel_tranalign_unique.fa 1>/dev/null 2>/dev/null

#~/bin/mutnumbers.pl query.out-mitocode_sel_tranalign_unique.fa 1>$SPNAME.$GENE.mutnumbers 2>/dev/null

#java -jar ~/bin/readseq.jar -a -f Phylip -o query.out-mitocode_sel_tranalign.phy query.out-mitocode_sel_tranalign_unique.fa 1>/dev/null 2>/dev/null

#~/bin/raxmlHPC-PTHREADS-SSE3 -x 987654 -p 987654 -T 4 -N 50 -f a -s query.out-mitocode_sel_tranalign.phy -n Rax_tree -m GTRGAMMAIX 1>raxmlHPC_out1 2>raxmlHPC_out2


python3 /home/agmikhaylova/termites/autoPipeline_simple.py /home/agmikhaylova/termites/newdb/cut_nucls.fasta COX2 > /mnt/lustre/agmikhaylova/termites/result.out

