# Enter your code here. Read input from STDIN. Print output to STDOUT
class Community:
    def __init__(self, n):
        self.data = [[i, 1] for i in range(n)]
        
    def find(self, x):
        y = x
        while self.data[y][0] != y:
            y = self.data[y][0]
            self.data[x][0] = y # to reduce the height of the tree
        return y
    
    def merge(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y: return
        self.data[root_y][0] = root_x
        self.data[root_x][1] += self.data[root_y][1]
        self.data[root_y][1] = 1
        
    def find_community_size(self, x):
        return self.data[self.find(x)][1]
    
def main():
    n,q = map(int, raw_input().split())
    c = Community(n)
    for _ in xrange(q):
        cmd = raw_input().split()
        if cmd[0] == 'Q': print c.find_community_size(int(cmd[1])-1)
        else: c.merge(int(cmd[1])-1, int(cmd[2])-1)
            
if __name__ == "__main__":
    main()
