def count_ways(M, N):
    # Initialize the DP table with zeros
    dp = [[0] * (M + 1) for _ in range(M + 1)]

    # Base case: There's one way to place 0 apples into any number of plates
    for i in range(M + 1):
        dp[i][0] = 1

    # Fill the DP table
    for i in range(1, M + 1):
        for j in range(1, min(i, N) + 1):
            dp[i][j] = dp[i][j - 1]  # Case where we do not use the j-th plate
            if i >= j:
                dp[i][j] += dp[i - j][j]  # Case where we use at least one apple in the j-th plate

    return dp[M][min(M, N)]  # The result is the minimum of M and N because we can't use more plates than apples


# Read input
t = int(input().strip())
results = []

for _ in range(t):
    M, N = map(int, input().strip().split())
    results.append(count_ways(M, N))

# Print results
for result in results:
    print(result)