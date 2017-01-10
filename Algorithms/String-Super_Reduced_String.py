# Enter your code here. Read input from STDIN. Print output to STDOUT
def reduce_str(s):
    st = []
    for c in s:
        if len(st) == 0 or st[-1] != c: st.append(c)
        else: st.pop()
    ret = ''.join(st) if len(st) > 0 else "Empty String"
    return ret
    
def main():
    print reduce_str(raw_input())

if __name__ == "__main__":
    main()
