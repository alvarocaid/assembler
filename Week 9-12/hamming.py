from functools import reduce 
import operator as op

def hamming_syndrome(bits):
    return reduce(
        op.xor,
        [i for (i, b) in enumerate(bits) if b]
    )

example_of_class = [0, 1, 1, 1, 1, 0, 0, 0, 1, 1] # First bit is not included since it is 0000
print(hamming_syndrome(example_of_class)) # 5

