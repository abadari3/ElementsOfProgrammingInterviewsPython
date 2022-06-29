# given a 64 bit integer, swap bits at indices i and j. 

# 0b11110000, 1, 5 -> 0b11010010
# O(1) time complexity
def brute_force(x: int, i: int, j: int) -> int:
    i_bit = (x>>i & 1)
    j_bit = (x>>j & 1)
    x &= ~(1 << i)
    x &= ~(1 << j)
    x |= (j_bit << i)
    x |= (i_bit << j)
    return x

# we can improve the above by only swapping when ith and jth bits are not equal
# we can also create an XOR mask to toggle bits as needed
def improved(x: int, i: int, j: int) -> int:
    if (x>>i & 1) != (x>>j & 1):
        mask = (1 << i) | (1 << j)
        x ^= mask
    return x
