# base_content 

Takes in a bedfile of coordinates and returns per position base composition.

## Requirements 
- python3
- bedtools (https://bedtools.readthedocs.io/en/latest/)
- numpy 
- pandas
- matplotlib
- scipy

### Installing on fiji
pip3 install scipy --user (the other modules are installed on fiji)

### Loading on fiji

module load bedtools

module load python/3.6.3

module load python/3.6.3/numpy

module load python/3.6.3/matplotlib

module load python/3.6.3/pandas

module load bedtools/2.25.0

### Running in the command line
```sh
python3 base_content -r /path/to/reference/hg38.fa -b ./my_bedfile.bed -o /output/dir/ -w 1500 -s experiment_name

```

Detailed documentation can be found here https://base-content.readthedocs.io/en/latest/index.html

Here are examples of plots generated:
![Example Plot](https://github.com/rutendos/base_content/blob/master/documentation/figs/SRX322989.tfit_greater_150bp.bed_BaseDistribution_All.png)

![Example Plot2](https://github.com/rutendos/base_content/blob/master/documentation/figs/SRX322989.tfit_greater_150bp.bed_SmoothedBaseDistribution_All.png)
