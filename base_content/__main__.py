import argparse
import main

parser = argparse.ArgumentParser(description = 'Calculating base content per position over a window.')

parser.add_argument('-r', '--reference', dest="ref", help = 'reference genome in fasta format', metavar="FILE")
parser.add_argument('-b', '--inbedfile', dest="inbed", help = 'input bed file', metavar="FILE")
parser.add_argument('-o', '--outdirectory', dest="outdir", help = 'directory for output', metavar="FILE")
#parser.add_argument('-d', '--outbedfile', dest="outbed", help = 'File name for output bed file', metavar="FILE")
#parser.add_argument('-f', '--outputfa', dest="outfasta", help = 'sequences of regions in fasta format', metavar="FILE")
parser.add_argument('-w', '--window', dest="window", help = 'window to extract sequences from', metavar="INT")

args = parser.parse_args()


#main.run(args.inbed, args.outbed, args.ref, args.outfasta,args.outdir, args.window)
main.run(args.inbed, args.ref, args.outdir, args.window)

##Example run
###python base_content -r /Users/rutendosigauke/Desktop/Dowell_Lab/genomes/hg38/hg38.fa -b /Users/rutendosigauke/Desktop/Dowell_Lab/projects/gc_content/test_bc/HO_P53_HUMAN.H10MO.B.bed.sorted.distance.bed -o /Users/rutendosigauke/Desktop/Dowell_Lab/projects/gc_content/test_bc/ -d /Users/rutendosigauke/Desktop/Dowell_Lab/projects/gc_content/test_bc/test_out.bed -f /Users/rutendosigauke/Desktop/Dowell_Lab/projects/gc_content/test_bc/test_out.fa -w 1500
