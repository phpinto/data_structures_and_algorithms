import time

def unique_paths_dp(m,n):
    paths = [[1] * n] * m
    for row in range(1,m):
        for col in range(1,n):
            paths[row][col] = paths[row - 1][col] + paths[row][col - 1]
    return paths[m-1][n-1]

start_time = time.time()
print(unique_paths_dp(7,3))
print(unique_paths_dp(12,9))
print(unique_paths_dp(16,16))
print(unique_paths_dp(55,36))
print(unique_paths_dp(100,100))
print(unique_paths_dp(250,123))
print(unique_paths_dp(1000,1000))
print("--- %s seconds ---" % (time.time() - start_time))