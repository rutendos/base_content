import argparse
import main

parser = argparse.ArgumentParser(description = 'Calculating base content per position over a window.')
requiredNamed = parser.add_argument_group('required named arguments')

parser.add_argument('-r', '--reference', dest="ref", help = 'reference genome in fasta format', metavar="FILE")
parser.add_argument('-b', '--inbedfile', dest="inbed", help = 'input bed file from TFEA or Tfit', metavar="FILE")
parser.add_argument('-o', '--outdirectory', dest="outdir", help = 'directory for output', metavar="FILE")
parser.add_argument('-w', '--window', dest="window",type=int, default=1500, help = 'window to extract sequences from (default = 1500)', metavar="INT")
parser.add_argument('-s', '--sample_name', dest="sample", help = 'name of the sample to be run', metavar="STR")
parser.add_argument('-t', '--is_tfea', dest="tfea",
                    help='Boolean operaror to indicate whether the bed file is from TFEA or Tfit (-t implies the bed file is from TFEA)',
                    action='store_true')

args = parser.parse_args()


main.run(args.inbed, args.ref, args.outdir, args.sample, args.tfea, args.window)

##Example run                                                                                                                                                          
###python base_content -r /Users/rutendosigauke/Desktop/Dowell_Lab/genomes/hg38/hg38.fa -b /Users/rutendosigauke/Desktop/Dowell_Lab/projects/gc_content/test_bc/HO_P53_HUMAN.H10MO.B.bed.sorted.distance.bed -o /Users/rutendosigauke/Desktop/Dowell_Lab/projects/gc_content/test_bc/ -w 1000 -s my_sample ##for non tfea bed file           
