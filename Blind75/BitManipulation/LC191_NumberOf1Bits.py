"""
191. Number of 1 Bits

Write a function that takes the binary representation of an unsigned integer 
and returns the number of '1' bits it has (also known as the Hamming weight).

Note:

Note that in some languages, such as Java, there is no unsigned integer type. 
In this case, the input will be given as a signed integer type. 

It should not affect your implementation, as the integer's internal binary 
representation is the same, whether it is signed or unsigned.

In Java, the compiler represents the signed integers using 2's complement notation. 
Therefore, in Example 3, the input represents the signed integer. -3.

Example 1:
Input: n = 00000000000000000000000000001011
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.

Example 2:
Input: n = 00000000000000000000000010000000
Output: 1
Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.

Example 3:
Input: n = 11111111111111111111111111111101
Output: 31
Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.
"""


def hammingWeight(n):
    """
    :type n: int
    :rtype: int
    """
    count = 0
    # Convert integer to binary string representation
    binary_representation = bin(n)
    for bit in binary_representation[2:]:  # Skip the '0b' prefix
        if bit == '1':
            count += 1

    return count


n1 = 0b00000000000000000000000000001011
n2 = 0b00000000000000000000000010000000
n3 = 0b11111111111111111111111111111101
print(3, hammingWeight(n1))
print(1, hammingWeight(n2))
print(31, hammingWeight(n3))


def hammingWeight2(n):
    """
    :type n: int
    :rtype: int
    """
    count = 0
    while n:
        count += n & 1
        n >>= 1

    return count


n1 = 0b00000000000000000000000000001011
n2 = 0b00000000000000000000000010000000
n3 = 0b11111111111111111111111111111101
print(3, hammingWeight2(n1))
print(1, hammingWeight2(n2))
print(31, hammingWeight2(n3))
