#-----------------------------------------
#outside imports
#-----------------------------------------

import os

class ExtractSequences:
    '''Extract sequences from fasta based on bed coordinates using bedtools'''
    # Initializer / Instance Attributes
    def __init__(self, reference, sample_name, outdir):
        self.reference = reference
        self.sample_name = sample_name
        self.outdir = outdir

    # instance method
    def get_sequences(self):

        os.system("bedtools getfasta -fi " + self.reference + " -bed " + self.outdir + self.sample_name + "_windowed_bed.bed" + " -fo " + self.outdir + self.sample_name + "_window_sequences.fa")#self.outfasta)
