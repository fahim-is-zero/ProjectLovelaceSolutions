# Input: Two integers A and B that have the value 0 or 1.
# Output: The output of a NAND gate with inputs A and B.

def NAND(A, B):
    val = {0 : False, 1 : True}
    A = val[A]
    B = val[B]

    nand = not (A and B)

    return nand

print(NAND(0,0))
