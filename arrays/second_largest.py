def second_largest(arr):
    if len(arr) < 2:
        return None
    if arr[0] <= arr[1]:
        second_largest, largest = arr[0], arr[1]
    else:
        second_largest, largest = arr[1], arr[0]
    for i in range(2,len(arr)):
        if arr[i] >= largest:
            second_largest = largest
            largest = arr[i]
    return second_largest

arr1 = [1,3,4,5,0,2]
arr2 = [55,89,1,2,3,4,6,0,2,0,1,4,6,7]
arr3 = [9,12,13,0,1,5,4,9,6,24,11,4,7]
arr4 = [5689,12,3456,89,7845,620,1233333333]
arr5 = [3,1]
arr6 = [88,56,89,41,563,124,496,785,121,634,120312]
arr7 = [2,2,1]
arr8 = [-2,-1]
arr9 = []
arr10 = []
print(second_largest(arr1))
print(second_largest(arr2))
print(second_largest(arr3))
print(second_largest(arr4))
print(second_largest(arr5))
print(second_largest(arr6))
print(second_largest(arr7))
print(second_largest(arr8))
print(second_largest(arr9))
print(second_largest(arr10))

def second_largest_2(arr):
    if len(arr) < 2:
        return None
    if arr[0] <= arr[1]:
        second_largest, largest = arr[0], arr[1]
    else:
        second_largest, largest = arr[1], arr[0]
    for i in range(2,len(arr)):
        if arr[i] > largest:
            second_largest = largest
            largest = arr[i]
        elif (arr[i] < largest) and ((second_largest < arr[i]) or (second_largest == largest)):
            second_largest = arr[i]
    return second_largest

print("------------------------")

arr1 = [2,2,2,2,2,2,1]
arr2 = [55,89,89,89,89,89,1,2,2,0,1,4,6,7]
arr3 = [9,12,13,0,1,5,4,9,6,24,11,4,7,]
arr4 = [1233333333,786,5689,12,3456,89,7845,620,1233333333,7846]
arr5 = [3,1,3,3,3,1,1,3,1,-2,0,0,0,3,1,-2,-5,-10,0]
arr6 = [-3,-3,-3,-3,-3,-3,-5689,-12,-3456,-89,-4,-3,-7845,-620,-1233333333,-2]
print(second_largest_2(arr1))
print(second_largest_2(arr2))
print(second_largest_2(arr3))
print(second_largest_2(arr4))
print(second_largest_2(arr5))
print(second_largest_2(arr6))
print(second_largest_2([1]))
print(second_largest_2([]))