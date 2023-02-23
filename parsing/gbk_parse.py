# Bringing in GenBank file

from Bio import SeqIO


for seq_record in SeqIO.parse("parsing/ls_orchid.gbk", "genbank"):
    print(seq_record.id)
    print(repr(seq_record.seq))
    print(len(seq_record))
