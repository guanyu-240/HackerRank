# Enter your code here. Read input from STDIN. Print output to STDOUT
a,z = ord('a'),ord('z')
A,Z = ord('A'),ord('Z')
zero = ord('0')

def f(c):
    if a <= c <= z: return c-a
    elif A <= c <= Z: return c-A+26
    elif (c-zero) % 2 == 1: return c-zero+52
    else: return c-zero+62
    
def main():
    s = raw_input()
    c_list = sorted(s, key=lambda x: f(ord(x)))
    ret = reduce(lambda x,y:x+y, c_list, "")
    print ret
    
if __name__ == "__main__":
    main()
