# Enter your code here. Read input from STDIN. Print output to STDOUT
import collections
def bfs(g, n, start):
    q = collections.deque()
    ret = [str(-1) for _ in xrange(n)]
    q.append(start)
    dist = 0
    count = 1
    while(len(q) > 0):
        start = q.popleft()
        count -= 1
        if ret[start] == "-1":
            ret[start] = str(dist*6)
            if g[start]:
                for x in g[start]:
                    if ret[x] == "-1": q.append(x)
        if count == 0: 
            count = len(q)
            dist += 1
    return filter(lambda x: x != '0', ret)

def solve():
    n,m = map(int, raw_input().split())
    g = [None for _ in xrange(n)]
    for _ in xrange(m):
        u,v = map(lambda x:int(x)-1, raw_input().split())
        if not g[u]: g[u] = []
        g[u].append(v)
        if not g[v]: g[v] = []
        g[v].append(u)
    start = int(raw_input())-1
    print ' '.join(bfs(g, n, start))

def main():
    t = int(raw_input())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
