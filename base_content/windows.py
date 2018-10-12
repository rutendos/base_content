#-----------------------------------------
#Outside imports
#-----------------------------------------

import pandas as pd

class BedWindows:



    # Initializer / Instance Attributes
    def __init__(self, bedfile, outdir, window = 1500):
        self.bedfile = bedfile
        self.outdir = outdir
        self.window = window

    # instance method
    #def get_windows(bedfile, outbed, window):
    def get_windows(self):
        '''This function takes in bed file sorted by TFEA and extends the window

        Attributes
        ----------
        bedfile : str
            path to bed file (tab delimited file from TFEA)

        outbed : str
            path to save output bed file (extension should be .bed)

        window : int
            the window size to extract from bedfile regions (default = 1500)

        Methods
        -------
        get_windows(bedfile, outbed, window=1500)
            obtains regions around the start and stop from input file of the
            window size.

        '''

        #bed = pd.read_table(self.bedfile, sep = '\t',header=None,
        #                       names = ["chr", "start", "stop",
        #                                "pval","fc","rank","chr_y",
        #                                "start_y","stop_y","seq",
        #                                "strand","vals","distance"])

        ##takes ranked_file.center.sorted.bed file from TFEA with 6 columns
        bed = pd.read_table(self.bedfile, sep = '\t',header=None,
                                  names = ["chr", "start", "stop",
                                            "pval","fc","rank"])


        bed_df = bed

        ##the -1500 position from "origin"
        bed_df["start"] = bed.apply(lambda x: x["start"] - int(self.window), axis=1)

        ##the 1500 position from the "origin"
        bed_df["stop"] = bed.apply(lambda x: x["stop"] + int(self.window), axis=1)

        ##sorting the data base on the rank
        bed_sort = bed_df.sort_values("rank")

        #############################################
        ##writing the new coordinates to a bedfile ##
        ##chr \t start \t stop \t rank_in_TFEA     ##
        #############################################

        #bed_sort.to_csv(self.outbed, sep='\t',
        bed_sort.to_csv(self.outdir + 'windowed_bed.bed', sep='\t',
                        columns=["chr","start","stop","rank"],
                        header = False, index = False)
