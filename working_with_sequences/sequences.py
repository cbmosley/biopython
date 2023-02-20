from Bio.Seq import Seq

# assigning value to my sequence of a genetic strand
# Seq object differs from the Python string in the methods it supports
# 5 prime 3 prime
my_seq = Seq("AGTACACTGGT")

print(my_seq)

# printing my sequence complement strand
# complement strand 3 prime to 5 prime
print(my_seq.complement())

# complement strand 5 prime to 3 prime
print(my_seq.reverse_complement())
