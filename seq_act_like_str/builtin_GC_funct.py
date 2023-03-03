from Bio.Seq import Seq
from Bio.SeqUtils import gc_fraction

# Bio.SeqUtils module has multiple GC functions built in


my_seq = Seq("GATCGATGGGCCTATAGGATCGAAAATCGC")

# Using this function should automatically cope with mixed case sequences and the ambiguous nucleotide S which means G or C
print(gc_fraction(my_seq))
