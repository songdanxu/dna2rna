import argparse

parse = argparse.ArgumentParser(description='Input and output file path.')

parse.add_argument('--input', '-i', help='The input file path.')
parse.add_argument('--output', '-o', help='The output file path.')

args = parse.parse_args()

from Bio import SeqIO


seq_id = []
seq_trna = []
for seq_record in SeqIO.parse(args.input, "fasta"):
    seq_id.append(seq_record.id)
    dna = seq_record.seq
    trna = dna.transcribe()
    seq_trna.append(trna)

print(seq_id)
print(seq_trna)
file = open(args.output, "w")
for i,k in enumerate(seq_id):
    file.write(">" + str(seq_id[i]) + '\n')
    file.write(str(seq_trna[i]) + '\n')
