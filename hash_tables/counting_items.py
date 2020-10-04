def count_items(arr):
    count_map = {}
    for i in arr:
        if i in count_map:
            count_map[i] += 1
        else:
            count_map[i] = 1
    return count_map

arr = [45,11,2,3,4,99,31,5,4,1,0,0,26,65,459,756,123,45,12,23,453,666,219,2]
print(count_items(arr))
arr = [1,2,3,4,5,6,7,8,9,10]
print(count_items(arr))
arr = [45,11,2,3,4,99,31,5]
print(count_items(arr))