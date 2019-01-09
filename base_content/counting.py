# Author: Rutendo F. Sigauke
#-------------------------------------
#Outside imports
#-------------------------------------
import pandas as pd
#from abc import ABCMeta, abstractmethod

# Parent class
class ListSequences:

    '''Get base content for multiple sequences various positions'''

    # Initializer / Instance Attributes
    def __init__(self, outdir, sample_name, sequence_length=3001):
        self.outdir = outdir
        self.sample_name = sample_name
        self.sequence_length = sequence_length

    # instance method
    #@abstractmethod
    def list_sequences(self):
        fasta_sequences = self.outdir + self.sample_name + "_window_sequences.fa"

        sequences = []
        sequence_names = []

        #add sequences and sequence names to lists
        with open(fasta_sequences) as fa:
            for line in fa:
                line = line.strip("\n")
                if ">" not in line:
                    sequences.append(line)
                else:
                    sequence_names.append(line)

        #return list with sequence
        return sequences

# Child class (inherits from GetSequences() class)
#class CountBases(ListSequences):
class CountBases:

    def __init__(self, sequences, outdir, sample_name, sequence_length=30001):
        self.sequences = sequences
        self.outdir = outdir
        self.sample_name = sample_name
        self.sequence_length = sequence_length

    # instance method
    #@abstractmethod
    def count_bases(self):
        '''calculate per position base composition across multiple
        sequences of even length.

        Parameters
        ----------
        seqs : list or array
            sequences of even lengths

        seq_len : int
            length of sequences (default=3001)

        Returns
        -------
        anew,tnew,cnew,gnew,nnew : list of lists
            normalized base counts for every position across all
            sequences

        '''

        ##initialize lists with length of sequences
        a = [0]*int(self.sequence_length)
        t = [0]*int(self.sequence_length)
        c = [0]*int(self.sequence_length)
        g = [0]*int(self.sequence_length)
        n = [0]*int(self.sequence_length)

        ##for each positions count the occurance of each base
        ##across all sequences in the the input list
        for i in range(int(self.sequence_length)):
            ##initialize counters
            count_a = 0
            count_t = 0
            count_c = 0
            count_g = 0
            count_n = 0
            for j in self.sequences:
                if j[i] == "a" or j[i] == "A":
                    count_a = count_a + 1
                    a[i] = count_a
                elif j[i] == "t" or j[i] == "T":
                    count_t = count_t + 1
                    t[i] = count_t
                elif j[i] == "g" or j[i] == "G":
                    count_g = count_g + 1
                    g[i] = count_g
                elif j[i] == "c" or j[i] == "C":
                    count_c = count_c + 1
                    c[i] = count_c
                elif j[i] == "n" or j[i] == "N":
                    count_n = count_n + 1
                    n[i] = count_n

        ##evenly distribute Ns across all bases
        nnew = [x / 4 for x in n]

        anew = [ai + bi for ai,bi in zip(a,nnew)]
        tnew = [ai + bi for ai,bi in zip(t,nnew)]
        gnew = [ai + bi for ai,bi in zip(g,nnew)]
        cnew = [ai + bi for ai,bi in zip(c,nnew)]

        ##get the base frequencies of all bases
        anew = [x / len(self.sequences) for x in anew]
        tnew = [x / len(self.sequences) for x in tnew]
        cnew = [x / len(self.sequences) for x in cnew]
        gnew = [x / len(self.sequences) for x in gnew]

        base_df = pd.DataFrame({'A': anew,
                                'T': tnew,
                                'G': cnew,
                                'C': gnew})

        #saving tab separared file as a tsv. 
        #file contains base content per position
        base_df.to_csv(self.outdir + self.sample_name +'_base_content.tsv', sep='\t')

        return anew, tnew, cnew, gnew, nnew
