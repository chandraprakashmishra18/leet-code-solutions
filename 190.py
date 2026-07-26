def reverseBits(n: int) -> int:
    res = 0
    for _ in range(32):
        # Shift result left to make space for the next bit
        res <<= 1
        # Add the least significant bit of n
        res |= (n & 1)
        # Shift n right to process the next bit
        n >>= 1
    return res