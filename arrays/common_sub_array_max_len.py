def common_sub_array_max_len(a, b):

    m = len(a)
    n = len(b)

    d = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if a[i-1] == b[j-1]:
                d[i][j] = d[i - 1][j - 1] + 1
            else:
                d[i][j] = max( d[i][j - 1],  d[i - 1][j])

    return d[-1][-1]

print(common_sub_array_max_len([1,3,5,6,7],[2,4,3,5,6]))
print(common_sub_array_max_len('abcdaf','acbcf'))

