# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
def most_common(s):
    c = Counter(s)
    return sorted(c.items(), key=lambda x:(-x[1], x[0]))[:min(len(c), 3)]

def main():
    s = raw_input()
    ret = most_common(s)
    for r in ret: print "{0} {1}".format(r[0], r[1])
                  
if __name__ == "__main__":
    main()
