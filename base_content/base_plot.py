#-----------------------------------------                                                                                                                 
#Outside imports                                                                                                                                           
#-----------------------------------------                                                                                                                 

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter

#-----------------------------------------                                                                                                                 
# Local imports                                                                                                                                            
#-----------------------------------------                                                                                                                 

from counting import *

def base_plot(seq, plottitle, outdir, sample_name, whichQ, window=None,q1=False, q4=False, q2_q3=False):
    '''plot line plot for each bases content across sequences for all/Q1/Q4                                                                                
    sequences on the same grid.                                                                                                                            
                                                                                                                                                           
    Parameters                                                                                                                                             
    ----------                                                                                                                                             
    seqs : list or array                                                                                                                                   
        sequences of even lengths                                                                                                                          
                                                                                                                                                           
    plottitle : str                                                                                                                                        
        title for the plot represented as a string                                                                                                         
                                                                                                                                                           
    q1 : bool                                                                                                                                              
        True or False inorder to plot Q1 sequences                                                                                                         
        (default = False)                                                                                                                                  
                                                                                                                                                           
    q4 : bool                                                                                                                                              
        True or False inorder to plot Q4 sequences                                                                                                         
        (default = False)                                                                                                                                  
                                                                                                                                                           
                                                                                                                                                           
    Returns                                                                                                                                                
    -------                                                                                                                                                
    line plot of choice                                                                                                                                    
    (all sequences, Q1 sequences or Q4 sequences)                                                                                                          
                                                                                                                                                           
    '''

    if q1:
        ##get percentiles for splitting the data into quatiles                                                                                                         
        quantile1 = round(np.percentile(np.arange(1, len(seq),1), 25))
        ##get sequences in Q1                                                                                                                                          
        seq_q1 = seq[0:int(quantile1)]
        counts = CountBases(seq_q1, int(window)).count_bases()
    if q4:
        ##get Q1 and Q3 boundaries                                                                                                                                     
        quantile3 = round(np.percentile(np.arange(1, len(seq),1), 75))
        ##get sequences in Q4                                                                                                                                          
        seq_q4 = seq[int(quantile3):len(seq)]
        counts = CountBases(seq_q4, int(window)).count_bases()
    if q2_q3:
        ##get percentiles for splitting the data into quatiles                                                                                                         
        quantile1 = round(np.percentile(np.arange(1, len(seq),1), 25))

        ##get Q1 and Q3 boundaries                                                                                                                                     
        quantile3 = round(np.percentile(np.arange(1, len(seq),1), 75))

        seq_q2q3 = seq[int(quantile1):int(quantile3)]
        counts = CountBases(seq_q2q3, int(window)).count_bases()
    else:
        counts = CountBases(seq, outdir,sample_name, int(window)).count_bases()

    ##get positions                                                                                                                                                    
    starting=int(window)
    stopping=int(window)+1
    positions = np.arange(-starting,stopping,1)

    #########################################                                                                                                                          
    ###Line plot for each base on one grid###                                                                                                                          
    #########################################                                                                                                                          
    plt.figure(figsize=(12,10))
    gs = plt.GridSpec(1, 1)
    ax0 = plt.subplot(gs[0])
    ax0.plot(positions,counts[0],color='blue', alpha=0.75, label='A')
    ax0.plot(positions,counts[1],color='purple', alpha=0.75, label='T')
    ax0.plot(positions,counts[2],color='orange', alpha=0.75, label = 'C')
    ax0.plot(positions,counts[3],color='red', alpha=0.75, label = 'G')
    ax0.set_xlabel('Distance (bp)',fontsize=30,fontweight='bold')
    ax0.set_ylabel('Base Content',fontsize=30,fontweight='bold')
    plt.xticks(fontsize = 25)
    plt.yticks(fontsize = 25)
    plt.legend(bbox_to_anchor=(1.05, 1),fontsize = 25, loc=2, borderaxespad=0.)
    plt.suptitle(plottitle, fontsize=40, fontweight='bold')
    plt.savefig(outdir + sample_name + '_BaseDistribution_'+str(whichQ)+'.png',bbox_inches='tight')
    plt.cla()


    #####################################################                                                                                                              
    ###Smooth the frequencies for better visualization###                                                                                                              
    #####################################################                                                                                                              

    a1 = savgol_filter(tuple(np.array(counts[0])), 61, 3) # window size 61, polynomial order 3                                                                 
    t1 = savgol_filter(tuple(np.array(counts[1])), 61, 3)
    c1 = savgol_filter(tuple(np.array(counts[2])), 61, 3)
    g1 = savgol_filter(tuple(np.array(counts[3])), 61, 3)

    plt.figure(figsize=(12,10))
    gs1 = plt.GridSpec(1, 1)
    ax1 = plt.subplot(gs1[0])

    ax1.plot(positions,a1,color='blue', alpha=0.75, label='A')
    ax1.plot(positions,t1,color='purple', alpha=0.75, label='T')
    ax1.plot(positions,c1,color='orange', alpha=0.75, label = 'C')
    ax1.plot(positions,g1,color='red', alpha=0.75, label = 'G')
    ax1.set_xlabel('Distance (bp)',fontsize=30,fontweight='bold')
    ax1.set_ylabel('Base Content',fontsize=30,fontweight='bold')
    plt.xticks(fontsize = 25)
    plt.yticks(fontsize = 25)
    plt.legend(bbox_to_anchor=(1.05, 1),fontsize = 25, loc=2, borderaxespad=0.)
    plt.suptitle(plottitle, fontsize=40, fontweight='bold')
    plt.savefig(outdir + sample_name + '_SmoothedBaseDistribution_'+str(whichQ)+'.png',bbox_inches='tight')
    plt.cla()

