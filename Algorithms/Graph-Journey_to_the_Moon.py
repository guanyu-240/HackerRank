from collections import deque

def store(l):
    adj = {}
    for i in xrange(l):
        a,b = map(int,raw_input().split())
        # Store a and b in an appropriate data structure
        if a in adj: adj[a].append(b)
        else: adj[a] = [b]
        if b in adj: adj[b].append(a)
        else: adj[b] = [a]
    return adj
        
def bfs(a, adj, visited):
    if visited[a]: return 0
    ret = 0
    q = deque([a])
    v = []
    while len(q) > 0:
        a = q.popleft()
        # special case: a appears 1+ times in the queue
        if visited[a]: continue
        visited[a] = True
        ret += 1
        if a not in adj: continue
        successors = adj[a]
        for s in successors:
            if not visited[s]: q.append(s)
    return ret
   
def main():    
    N,l = map(int,raw_input().split())
    visited = [False for _ in range(N)]
    adj = store(l)
    # Compute the final result using the inputs from above
    result = N*(N-1)/2
    for a in range(N):
        count = bfs(a, adj, visited)
        if count > 1: result -= count*(count-1)/2
    print result
    
if __name__ == "__main__":
    main()
