import time

def unique_paths(m,n):
    if m == 1 or n == 1:
        return 1
    else:
        return unique_paths(m - 1, n) + unique_paths(m, n - 1)

start_time = time.time()
print(unique_paths(7,3))
print(unique_paths(12,9))
print(unique_paths(16,16))
print("--- %s seconds ---" % (time.time() - start_time))