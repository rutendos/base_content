#----------------------------------------
# Outside imports
#----------------------------------------

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#----------------------------------------
# Local imports
#----------------------------------------

from windows import *
from get_sequences import *
from counting import *
from base_plot import *

def run(bedfile, reference, outdir, sample_name, tfea, window=1500, sequence_length=3001):

    if tfea:
        print("---------Expanding TFEA bed Windows----------")
        bedwindows = BedWindows(bedfile, outdir, sample_name, int(window))
        bedwindows.get_windows()
    else:
        print("------------Bed file not from TFEA------------")
        print("--------------Expanding Windows---------------")
        bedwindows = BedWindows(bedfile, outdir, sample_name, int(window))
        bedwindows.get_tfit_windows()

    print("-------------Extracting Sequences-------------")    
    seqs = ExtractSequences(reference, sample_name, outdir)
    seqs.get_sequences()
    
    print("-----------Counting Base Content-------------")
    listseq = ListSequences(outdir, sample_name)
    window_seq = listseq.list_sequences()

    print("--------------Plot Generation----------------")
    base_plot(window_seq,"Base Content "+sample_name, outdir, sample_name, "All",int(sequence_length))

    
    ##TO DO: incooporate quartiles...
    #base_plot(window_seq,"Q1 Content "+ sample_name, outdir, "Q1", int(sequence_length), q1 = True)

    #base_plot(window_seq,"Q4 Content "+ sample_name, outdir, "Q4", int(sequence_length), q4 = True)

    #base_plot(window_seq,"Q2 and Q3 Content "+ sample_name, outdir, "Q2_Q3", int(sequence_length), q2_q3 = True)
