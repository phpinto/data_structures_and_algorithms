def find_max(items):
    if len(items) == 1:
        return items[0]
    else:
        first = items[0] 
        rest = find_max(items[1:])

        if (first >= rest):
            return first
        else:
            return rest


arr = [45,11,2,3,4,99,31,5,4,1,0,0,26,65,459,756,123,45,12,23,453,666,219,2]
print(find_max(arr))
arr = [1,2,3,4,5,6,7,8,9,10]
print(find_max(arr))
arr = [45,11,2,3,4,99,31,5]
print(find_max(arr))
arr = [2,3,4,6,88,90,120,256,623,1000,5161212321,2]
print(find_max(arr))