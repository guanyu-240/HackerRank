#!/bin/python
# Ax = 1^2....(x-1)^x
# The result is XOR(0,l)^XOR(0,l+1)^...^XOR(0,r-1)^XOR(0,r)
# if r % 2 == 0, l % 2 != 0: ret = r^(r-2)^(r-4)^...^(l+3)^(l+1)
# if r % 2 == 0, l % 2 == 0: ret = r^(r-2)^(r-4)^...^(l+2)^l^XOR(0, l-1)
# if r % 2 != 0, l % 2 != 0: ret = XOR(0,r)^(r-1)^(r-3)^...^(l+3)^(l+1)
# if r % 2 != 0, l % 2 == 0: ret = XOR(0,r)^(r-1)^(r-3)^...^(l+2)^(l)^XOR(l-1)

#Note XOR(0,2n by 1) = 2*XOR(0,n by 1)
import sys

def xor_to_n(n):
    mod = n%4
    if mod == 0: return n
    elif mod == 3: return 0
    elif mod == 2: return n+1
    else: return 1
          
def sequence_sum(l, r):
    ret = 0
    if r % 2 != 0: 
        ret ^= xor_to_n(r)
    ret ^= 2*(xor_to_n(r/2) ^ xor_to_n((l+1)/2-1))  
    if l % 2 == 0:
        ret ^= xor_to_n(l-1)
    return ret

Q = int(raw_input().strip())
for a0 in xrange(Q):
    L,R = raw_input().strip().split(' ')
    L,R = [long(L),long(R)]
    print sequence_sum(L,R)
