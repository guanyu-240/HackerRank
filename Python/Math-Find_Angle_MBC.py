# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import degrees,atan

def mbc(x1, x2):
    return u"{}\xb0".format(int(round(degrees(atan(float(x1)/float(x2))))))

def main():
    x1 = raw_input()
    x2 = raw_input()
    print mbc(x1, x2)

if __name__ == "__main__":
    main()
