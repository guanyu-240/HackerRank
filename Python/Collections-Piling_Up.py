# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
import sys

def canPileUp(cubes):
    if len(cubes) == 0: return 'No'
    e = cubes.pop()
    while len(cubes) > 0 and e >= cubes[-1]: e = cubes.pop()
    if len(cubes) == 0: return 'Yes'
    e = cubes.popleft()
    while len(cubes) > 0 and e >= cubes[0]: e = cubes.popleft()
    return 'Yes' if len(cubes) == 0 else 'No'
    
def main():
    t = int(sys.stdin.readline().strip())
    for _ in xrange(t):
        n = int(sys.stdin.readline())
        print canPileUp(deque(map(int, sys.stdin.readline().strip().split())))

if __name__ == "__main__":
    main()
