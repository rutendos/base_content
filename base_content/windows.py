#-----------------------------------------
#Outside imports
#-----------------------------------------

import pandas as pd

class BedWindows:



    # Initializer / Instance Attributes
    def __init__(self, bedfile, outdir, sample_name, window = 1500):
        self.bedfile = bedfile
        self.outdir = outdir
        self.sample_name = sample_name
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

        bed_sort.to_csv(self.outdir + self.sample_name + '_windowed_bed.bed', sep='\t',
                        columns=["chr","start","stop","rank"],
                        header = False, index = False)

    # instance method
    #def get_windows(bedfile, outbed, window):
    def get_tfit_windows(self):
        '''This function takes in bed files from Tfit redefines mu and extends the window
        '''

        ##takes ranked_file.center.sorted.bed file from TFEA with 6 columns
        bed = pd.read_table(self.bedfile, sep = '\t',header=None,
                            names = ["chr", "start", "stop"])

        bed_df = bed

        #bed_int["range"] = bed_int["stop"] - bed_int["start"]

        #bed_df = bed_int.loc[bed_int["range"] >= 500]

        ##redesignate mu to get new start and stop coordinates
        bed_df["start_new"] = bed_df.apply(lambda x: round((x["start"] + x["stop"])/2), axis=1)

        bed_df["stop_new"] = bed_df.apply(lambda x: x["start_new"] + 1, axis = 1)

        ##the -1500 position from "origin"
        bed_df["start"] = bed.apply(lambda x: x["start_new"] - int(self.window), axis=1)

        ##the 1500 position from the "origin"
        bed_df["stop"] = bed.apply(lambda x: x["stop_new"] + int(self.window), axis=1)

        ##saving the new bedfile
        bed_df.to_csv(self.outdir + self.sample_name + '_windowed_bed.bed', sep='\t',
                        columns=["chr","start","stop"],
                        header = False, index = False)                        