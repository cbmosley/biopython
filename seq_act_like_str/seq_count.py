from Bio.SeqUtils import gc_fraction
from Bio.Seq import Seq

my_seq = Seq("GATCGATGGGCCTATATAGGATCGAAAATCGC")

print(len(my_seq))

print(my_seq.count("G"))

# getting GC percentage of sequence (aka nitrogenous bases)

print("This is my GC Percentage of my DNA sequence")
print(100 * (my_seq.count("G") + my_seq.count("C")) / len(my_seq))


