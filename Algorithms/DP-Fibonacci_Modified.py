# Enter your code here. Read input from STDIN. Print output to STDOUT
def fibonacci_modified(f1, f2, n):
    dp = [0 for _ in range(n)]
    dp[0],dp[1] = f1,f2
    for i in range(2, n):
        dp[i] = dp[i-1]**2+dp[i-2]
    return dp[-1]

print fibonacci_modified(*map(int, raw_input().split()))
