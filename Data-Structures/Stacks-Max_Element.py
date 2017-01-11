# Enter your code here. Read input from STDIN. Print output to STDOUT
def process_query(st, st_max, query):
    if query[0] == 1:
        st.append(query[1])
        if len(st_max) == 0 or query[1] >= st_max[-1]:
            st_max.append(query[1])
    elif query[0] == 2:
        if len(st) == 0: return
        x = st.pop()
        if st_max[-1] == x: st_max.pop()
    else:
        if len(st) == 0: print 'EMPTY!'
        else: print st_max[-1]

def main():
    st = []
    st_max = []
    n = int(raw_input())
    for _ in range(n):
        process_query(st, st_max, map(int, raw_input().split()))

if __name__ == "__main__":
    main()
