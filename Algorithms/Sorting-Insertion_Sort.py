#!/bin/python
def insertionSort(ar):
    ret = ""
    n = len(ar)
    for i in range(n-1):
        j = i
        while j >= 0 and ar[j] > ar[j+1]:
            x = ar[j+1]
            ar[j+1] = ar[j]
            print ' '.join(map(str, ar))
            ar[j] = x
            j -= 1
    print ' '.join(map(str, ar))

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)
