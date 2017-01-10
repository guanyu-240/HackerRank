# Enter your code here. Read input from STDIN. Print output to STDOUT
def counter_game(N):
    if N <= 1: return 'Louise'
    count = 0
    mask = 1
    one_detected = False
    for _ in range(64):
        if (mask & N) == mask:
            if not one_detected: one_detected = True
            else: count += 1
        elif not one_detected: count += 1
        mask <<= 1
    return 'Louise' if count%2 == 1 else "Richard"

def main():
    T = int(raw_input())
    for _ in xrange(T):
        N = int(raw_input())
        print counter_game(N)
        
if __name__ == "__main__":
    main()
