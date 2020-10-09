def rotated_search(arr,left_ptr, right_ptr, k): 
    if left_ptr > right_ptr:
        return -1
    
    mid = (left_ptr + right_ptr) // 2
    
    if arr[mid] == k:
        return mid
        
    if arr[left_ptr] <= arr[mid]:
        if k >= arr[left_ptr] and k < arr[mid]:
            return rotated_search(arr,left_ptr, mid - 1, k)
        else:
            return rotated_search(arr,mid + 1, right_ptr, k)
    else:
        if k > arr[mid] and k <= arr[right_ptr]:
            return rotated_search(arr,mid + 1, right_ptr, k)
        else:
            return rotated_search(arr,left_ptr, mid - 1, k)
    
    
arr = [4, 5, 6, 7, 8, 9, 1, 2, 3] 
key = 6
i = rotated_search(arr, 0, len(arr)-1, key) 
if i != -1: 
    print ("Index: % d"% i) 
else: 
    print ("Key not found") 

arr = [3, 4, 5, 6, 1, 2] 
key = 1
i = rotated_search(arr, 0, len(arr)-1, key) 
if i != -1: 
    print ("Index: % d"% i) 
else: 
    print ("Key not found") 

arr = [5, 6, 7, 8, 9, 10, 1, 2, 3] 
key = 10
i = rotated_search(arr, 0, len(arr)-1, key) 
if i != -1: 
    print ("Index: % d"% i) 
else: 
    print ("Key not found") 

arr = [3, 1, 2] 
key = 1
i = rotated_search(arr, 0, len(arr)-1, key) 
if i != -1: 
    print ("Index: % d"% i) 
else: 
    print ("Key not found") 

arr = [3, 5, 1, 2] 
key = 6
i = rotated_search(arr, 0, len(arr)-1, key) 
if i != -1: 
    print ("Index: % d"% i) 
else: 
    print ("Key not found") 