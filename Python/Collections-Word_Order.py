# Enter your code here. Read input from STDIN. Print output to STDOUT

def main():
    m = {}
    n = int(raw_input())
    for i in xrange(n):
        w = raw_input()
        if w in m: m[w][1] += 1
        else: m[w] = [i, 1]
    print str(len(m)) + '\n' + ' '.join(map(lambda x:str(x[1]), sorted(m.values())))

if __name__ == "__main__":
    main()
