from Bio.Seq import Seq

# assigning value to my sequence of a genetic strand
my_seq = Seq("AGTACACTGGT")
print(my_seq)
# printing my sequence complement strand
print(my_seq.complement())
