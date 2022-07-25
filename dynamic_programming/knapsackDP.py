def knapsackDP(values, weights, max_weight):

    n = len(values)
    dp = [[0 for x in range(max_weight + 1)] for x in range(n+1)]

    for i in range(n+1):
        for w in range(max_weight + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(values[i-1] + dp[i-1][w-weights[i-1]],
                               dp[i-1][w])

            else:
                dp[i][w] = dp[i-1][w]
    return dp[n][max_weight]