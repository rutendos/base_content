#----------------------------------------
# Outside imports
#----------------------------------------

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#from abc import ABCMeta, abstractmethod

#----------------------------------------
# Local imports
#----------------------------------------

from windows import *
from get_sequences import *
from counting import *
from base_plot import *

def run(bedfile, reference, outdir, window=1500, sequence_length=3001):

    print("--------------Expanding Windows---------------")
    ##get_windows(bedfile, outbed, int(window))
    bedwindows = BedWindows(bedfile, outdir, int(window))
    bedwindows.get_windows()

    print("-------------Extracting Sequences-------------")    
    #ExtractSequences(reference, outbed, outfasta)
    seqs = ExtractSequences(reference, outdir)
    seqs.get_sequences()
    
    print("-----------Counting Base Content-------------")
    listseq = ListSequences(outdir)
    window_seq = listseq.list_sequences()

    

    #check how you want the plots made
    ##counter = CountBases(window_seq, int(sequence_length))
    ##counted_bases = counter.count_bases()

    print("--------------Plot Generation----------------")
    base_plot(window_seq,"Base Content", outdir, "All",int(sequence_length))

    

    #base_plot(window_seq,"Q1 Content", outdir, "Q1", int(sequence_length), q1 = True)

    #base_plot(window_seq,"Q4 Content", outdir, "Q4", int(sequence_length), q4 = True)

    #base_plot(window_seq,"Q2 and Q3 Content", outdir, "Q2_Q3", int(sequence_length), q2_q3 = True)
