#!/bin/bash                                                                                                                                                    

###Name the job                                                                                                                                      
#SBATCH --job-name=Allen2014_ATGC  

###Specify the queue                                                                         
#SBATCH -p short                                                                                                                                               

###Specify WallTime                                                                          
#SBATCH --time=2:00:00                                                                                                                                        

### Specify the number of nodes/cores                                                        
#SBATCH --nodes=1                                                                                                                                              
#SBATCH --ntasks=1                                                                                                                                  

### Allocate the amount of memory needed                                                                                                                      
#SBATCH --mem=250gb                                                                                                                                            

### Setting to mail when the job is complete                           
#SBATCH --error /scratch/Users/rusi2317/projects/gc_content/e_and_o/%x.err                                                                         
#SBATCH --output /scratch/Users/rusi2317/projects/gc_content/e_and_o/%x.out                                                                        

### Set your email address                                                                                                                                     
#SBATCH --mail-type=ALL                                                                                                                                        
#SBATCH --mail-user=rutendo.sigauke@ucdenver.edu  

module purge
module load python/3.6.3
module load python/3.6.3/numpy
module load python/3.6.3/matplotlib
module load python/3.6.3/pandas
module load bedtools/2.25.0

BIN=/scratch/Users/rusi2317/projects/gc_content/bin

OUTDIR=/scratch/Users/rusi2317/projects/gc_content/analysis/Allen2014_v2

GENOME=/scratch/Users/rusi2317/projects/gc_content/genome

BED=/scratch/Users/rusi2317/projects/tfea/output/Allen2014/TFEA_DMSO_1hr-Nutlin_1hr_3/temp_files

NAME=Allen2014_width1000

##run the base_content

python3 ${BIN}/base_content//base_content -r ${GENOME}/hg19.fa -b ${BED}/ranked_file.center.sorted.bed -o ${OUTDIR}/ -l 2001 -w 1000 -s ${NAME} -t
