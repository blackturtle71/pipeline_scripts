from Bio import SeqIO
import re
import subprocess
def to_dict_remove_dups(sequences):
                return {record.id: record.seq for record in sequences}
Sequences=to_dict_remove_dups(SeqIO.parse("COX2taxid.fasta","fasta"))
for Seq in Sequences:
        species_name = Seq
        value = Sequences[Seq]
        #list_of_s = []
        with open('nuc_seq.fa', 'w+') as nucl:
            nucl.write('>{0}\n{1}\n'.format(species_name, value))

        subprocess.call("/usr/bin/transeq -sequence nuc_seq.fa -outseq prot_seq.pep -frame 6 -table 5", shell=True)

        with open('nuc_seq.fa', 'r') as i:
                nuc_line = i.readlines()
                the_string = "".join(map(str.strip, nuc_line))
                slicing_nuc = re.sub(r'(>\d+_taxon:\d+)', r'\g<1>;', the_string)
                sliced_nuc = slicing_nuc.split(';')
                name_nuc = sliced_nuc[0]
                s_nuc = sliced_nuc[1]
                #list_of_s.append(s_nuc)

        '''with open('prot_seq.pep') as prot:
                lines = prot.readlines()
                protein = "".join(map(str.strip, lines))
                prot_multi_str = re.sub('>', '\n>', protein)
                prot_list = prot_multi_str.splitlines()
                del prot_list[0]
                for l in prot_list:
                        slicing = re.sub(r'(_\d+)', r'\g<1>:', l)
                        sliced = slicing.split(':')
                        name = sliced[0]
                        s = '\n' + sliced[1]
                        s = re.sub(r'\n', r'', s)
                        list_of_s.append(s)
        print(list_of_s)'''

        with open('prot_seq.pep') as prot:
                lines = prot.readlines()
                protein = "".join(map(str.strip, lines))
                prot_multi_str = re.sub('>', '\n>', protein)
                prot_list = prot_multi_str.splitlines()
                del prot_list[0]
                list_of = []
                for l in prot_list:
                        list_of.append(l.count('*'))
                #ALWAYS DELETE prior cut_nucls.fasta!
                with open('cut_nucls.fasta', 'a+') as cut:
                        cut.write(name_nuc)
                        if list_of.index(min(list_of)) == 1:
                                chopped = '\n' + s_nuc[1:] + '\n'
                                cut.write(chopped)
                        elif list_of.index(min(list_of)) == 2:
                                chopped = '\n' + s_nuc[2:] + '\n'
                                cut.write(chopped)
                        else:
                                cut.write('\n' + s_nuc + '\n')







