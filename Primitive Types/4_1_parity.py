# compute the parity (number of set bits) of a very large number of 64-bit words.
from numpy import mask_indices

# iterate bit by bit, counting 1s.
# O(n) time complexity, where n is number of bits.
def brute_force(x: int) -> int:
    res = 0
    while x:
        res ^= x&1
        x >>= 1
    return res

# improve by skipping 0 bits for each iteration.
# O(k) time complexity, where k is number of set bits. 
def brute_force_improvement(x: int) -> int:
    res = 0
    while x:
        res ^= 1
        x &= (x-1)
    return res

# use caching to improve scalability
# suppose we cache L-bit inputs, then we split n bits into n/L constant calculations
# O(n/L) time complexity, where cached words are L bits.
PRECOMPUTED_PARITY = [] # precomputed cache. Not empty in real world usage
def lookup_table(x: int) -> int:
    mask_size = 16
    bit_mask = 0xFFFF
    res = PRECOMPUTED_PARITY[x >> (3 * mask_size)]
    res ^= PRECOMPUTED_PARITY[x >> (2 * mask_size) & bit_mask]
    res ^= PRECOMPUTED_PARITY[(x >> mask_size) & bit_mask]
    res ^= PRECOMPUTED_PARITY[x & bit_mask]
    return res

# since XOR is associative, order does not matter.
# note that the parity of any x is the same as the XOR'd parity of each half of x. 
# thus, we can reduce the number of bits in x by half every time we calculate parity.
# O(log n) time complexity
def parallel_operations(x: int) -> int:
    # assume we are operating in 64-bit integers.
    x ^= (x >> 32)
    x ^= (x >> 16)
    x ^= (x >> 8)
    x ^= (x >> 4)
    x ^= (x >> 2)
    x ^= (x >> 1)
    return x&1

# VARIANTS
# Right Propagate the rightmost set bit in x. 
# 0b01010000 --> 0b01011111
def right_propagate(x: int) -> int:
    return x|((x&~(x-1))-1)

# Compute x mod a power of 2
# 77 mod 64 --> 13
def mod_power_2(x: int, p: int) -> int:
    return x & ((1<<p) - 1)

# Test if x is a power of two
# returns True for x = 1, 2, 4, 8, ... and otherwise False
def is_power_of_two(x: int) -> bool:
    return x&(x-1) == 0 
