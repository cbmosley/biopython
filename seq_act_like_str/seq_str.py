from Bio.Seq import Seq

my_seq = Seq("GATCG")

for index, letter in enumerate(my_seq):
    print("%i %s" % (index, letter))

print(len(my_seq))

# You can access elements of the sequence in the same way as for strings

print(my_seq[0])
