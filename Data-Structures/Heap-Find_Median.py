#!/bin/python

import sys
from heapq import heappush,heappop

def findMedian(a):
    lower,higher = [],[]
    median = 0.0
    for num in a:
        x = long(num)
        if len(lower) == 0:
            heappush(lower, x*(-1))
            median = float(x)
        else:
            if x >= lower[0]*(-1):
                heappush(higher, x)
                if len(higher) - len(lower) > 1:
                    heappush(lower, heappop(higher)*(-1))
            else:
                heappush(lower, x*(-1))
                if len(lower) - len(higher) > 1:
                    heappush(higher, heappop(lower)*(-1))
            if len(lower) == len(higher):
                median = float((-1)*lower[0]+higher[0])/2.0
            elif len(lower) > len(higher):
                median = float(lower[0]*(-1))
            else:
                median = float(higher[0])
        print '{:0.1f}'.format(median) 
            
        

N = int(raw_input().strip())
a = []
a_i = 0
for a_i in xrange(N):
    a_t = int(raw_input().strip())
    a.append(a_t)
findMedian(a)
