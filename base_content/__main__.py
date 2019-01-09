import argparse
import main

parser = argparse.ArgumentParser(description = 'Calculating base content per position over a window.')

requiredNamed = parser.add_argument_group('required named arguments')
requiredNamed.add_argument('-r', '--reference', dest="ref", help = 'reference genome in fasta format', metavar="FILE", required=True)
#parser.add_argument('-r', '--reference', dest="ref", help = 'reference genome in fasta format', metavar="FILE", required=True)
requiredNamed.add_argument('-b', '--inbedfile', dest="inbed", help = 'input bed file from TFEA or Tfit', metavar="FILE", required=True)
#parser.add_argument('-b', '--inbedfile', dest="inbed", help = 'input bed file from TFEA or Tfit', metavar="FILE", required=True)
requiredNamed.add_argument('-o', '--outdirectory', dest="outdir", help = 'directory for output', metavar="DIR", required=True)
parser.add_argument('-w', '--window', dest="window",type=int, default=1500, help = 'window to extract sequences from', metavar="INT")
parser.add_argument('-l', '--seq_len', dest="length_seq", type=int, default=3001, help='width of window around mu.', metavar='INT')
requiredNamed.add_argument('-s', '--sample_name', dest="sample", help = 'name of the sample to be run', metavar="STR", required=True)
parser.add_argument('-t', '--is_tfea', dest="tfea", 
                    help='Boolean operaror to indicate whether the bed file is from TFEA or Tfit (-t means bed file is from TFEA)', 
                    action='store_true')

args = parser.parse_args()


main.run(args.inbed, args.ref, args.outdir, args.sample, args.tfea, args.window, args.length_seq)

##Example run
###python base_content -r /Users/rutendosigauke/Desktop/Dowell_Lab/genomes/hg38/hg38.fa -b /Users/rutendosigauke/Desktop/Dowell_Lab/projects/gc_content/test_bc/HO_P53_HUMAN.H10MO.B.bed.sorted.distance.bed -o /Users/rutendosigauke/Desktop/Dowell_Lab/projects/gc_content/test_bc/ -d /Users/rutendosigauke/Desktop/Dowell_Lab/projects/gc_content/test_bc/test_out.bed -f /Users/rutendosigauke/Desktop/Dowell_Lab/projects/gc_content/test_bc/test_out.fa -w 1500
