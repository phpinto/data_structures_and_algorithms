def eliminate_duplicates(arr):
    hash_table = {}
    for i in range(len(arr)):
        if arr[i] not in hash_table:
            hash_table[arr[i]] = i
    return hash_table.keys()

def eliminate_duplicates_set(arr):
    hash_set = set()
    for i in range(len(arr)):
        if arr[i] not in hash_set:
            hash_set.add(arr[i])
    return list(hash_set)

arr = [45,11,2,3,4,99,31,5,4,1,0,0,26,65,459,756,123,45,12,23,453,666,219,2]
print(arr)
print(eliminate_duplicates(arr))
arr = [1,2,3,4,5,6,7,8,9,10]
print(arr)
print(eliminate_duplicates(arr))
arr = [45,11,2,3,4,99,31,5]
print(arr)
print(eliminate_duplicates(arr))

arr = [45,11,2,3,4,99,31,5,4,1,0,0,26,65,459,756,123,45,12,23,453,666,219,2]
print(arr)
print(eliminate_duplicates_set(arr))
arr = [1,2,3,4,5,6,7,8,9,10]
print(arr)
print(eliminate_duplicates_set(arr))
arr = [45,11,2,3,4,99,31,5]
print(arr)
print(eliminate_duplicates_set(arr))