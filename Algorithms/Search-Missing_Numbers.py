# Enter your code here. Read input from STDIN. Print output to STDOUT
import collections

def missing_numbers(A, B):
    counter = collections.Counter(B)
    for x in A: counter[x] -= 1
    ret_list = map(lambda x:str(x[0]), filter(lambda y: y[1]>0, counter.items()))
    ret_list.sort()
    return ret_list
        

def main():
    n = int(raw_input())
    A = map(int, raw_input().split())
    m = int(raw_input())
    B = map(int, raw_input().split())
    print ' '.join(missing_numbers(A,B))

if __name__ == "__main__":
    main()
