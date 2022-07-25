from heapq import nsmallest

def get_kth_smallest(k, arr):
    max_level = min(k, len(arr))
    return nsmallest(k, [x for row in arr[:max_level][:max_level] for x in row])[-1]

arr = [[1,4,7],[3,5,9],[6,8,11]]
print(get_kth_smallest(4, arr))
print(get_kth_smallest(2, arr))
print(get_kth_smallest(1, arr))