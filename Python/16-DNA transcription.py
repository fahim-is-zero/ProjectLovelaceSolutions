# Input: A string of ATCG characters representing a DNA sequence.
# Output: The RNA sequence corresponding to the input DNA sequence.


def rna(dna):

    RNA = dna.replace("T", "U")

    return RNA[::-1]

print(rna("CCTAGGACCAGGTT"))
