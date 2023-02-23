# Simple FASTA parsing example

from Bio import SeqIO

for seq_record in SeqIO.parse("parsing/ls_orchid.fasta", "fasta"):
    print(seq_record.id)
    print(repr(seq_record.seq))
    print(len(seq_record))
