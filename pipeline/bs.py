from Bio import SeqIO
import re
import subprocess
def to_dict_remove_dups(sequences):
    return {re.sub('>\d+_', '> ', record.id): record.seq for record in sequences}
Sequences=to_dict_remove_dups(SeqIO.parse("test.fasta","fasta"))
for Seq in Sequences:
        species_name = Seq
        value = Sequences[Seq]
        with open('nuc_seq.fa', 'w+') as nucl:
            nucl.write('>{0}\n{1}\n'.format(species_name, value))

        subprocess.call("/usr/bin/transeq -sequence nuc_seq.fa -outseq prot_seq.pep -frame 6 -table 5", shell=True)

        with open('prot_seq.pep') as prot:
                lines = prot.readlines()
                protein = "".join(map(str.strip, lines))
                prot_multi_str = re.sub('>', '\n>', protein)
                prot_list = prot_multi_str.splitlines()
                del prot_list[0]
                list_of = []
                for l in prot_list:
                        list_of.append(l.count('*'))
                the_min = '\n' + prot_list.pop(list_of.index(min(list_of)))
                the_min = re.sub(r'(_\d+)', r'\g<1>:', the_min)
                that_one = the_min.split(':')
                name = '>' + species_name
                s = '\n' + that_one[1]

                #always DELETE prior prot_no_bs before start
                '''with open('proper_names.fasta', 'a+') as out:
                        out.write(name)
                        out.write(s)'''
                print(species_name)





