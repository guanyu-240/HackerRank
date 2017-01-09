#!/usr/bin/py
# Head ends here
from sets import Set
def pairs(a,k):
    #a contains array of numbers and k is the value of difference
    s = Set([])
    answer = 0
    for x in a:
        if x+k in s: answer += 1
        if x-k in s: answer += 1
        s.add(x)
    return answer
# Tail starts here
if __name__ == '__main__':
    a = map(int, raw_input().strip().split(" "))
    _a_size=a[0]
    _k=a[1]
    b = map(int, raw_input().strip().split(" "))
    print pairs(b,_k)
