#-----------------------------------------
#outside imports
#-----------------------------------------

import os

class ExtractSequences:
    '''Extract sequences from fasta based on bed coordinates using bedtools'''
    # Initializer / Instance Attributes
    def __init__(self, reference, outdir):
        self.reference = reference
        self.outdir = outdir

    # instance method
    def get_sequences(self):

        os.system("bedtools getfasta -fi " + self.reference + " -bed " + self.outdir + "windowed_bed.bed" + " -fo " + self.outdir + "window_sequences.fa")#self.outfasta)
