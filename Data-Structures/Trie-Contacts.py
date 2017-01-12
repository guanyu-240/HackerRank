# Enter your code here. Read input from STDIN. Print output to STDOUT
trie = {}
def add(s):
    node = trie
    for c in s:
        if c not in node:
            node[c] = {"count": 0}
        node = node[c]
        node["count"] += 1
        
def search(s):
    node = trie
    for c in s:
        if c not in node: return 0
        node = node[c]
    return node["count"]

def main():
    n = int(raw_input())
    for _ in range(n):
        op, w = raw_input().split()
        if op == "find": print search(w)
        else: add(w)
            
if __name__ == "__main__":
    main()
