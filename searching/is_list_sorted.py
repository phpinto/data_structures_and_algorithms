def is_list_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i + 1] < arr[i]:
            return False
    return True


print(is_list_sorted([45,11,2,3,4,99,31,5,4,1,0,0,26,65,459,756,123,45,12,23,453,666,219,2]))
print(is_list_sorted(sorted([45,11,2,3,4,99,31,5,4,1,0,0,26,65,459,756,123,45,12,23,453,666,219,2])))
print(is_list_sorted([2,6,4,0,1,26,354,10,0,89]))
print(is_list_sorted([2,3,4,6,88,90,120,256,623,1000,5161212321]))
print(is_list_sorted([2,3,4,6,88,90,120,256,623,1000,5161212321,2]))
