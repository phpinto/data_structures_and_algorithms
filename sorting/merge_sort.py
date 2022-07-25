def merge_sort(data):
    if len(data) > 1:
        mid_point = len(data)//2
        left = data[:mid_point]
        right = data[mid_point:]
        merge_sort(left)
        merge_sort(right)

        i,j,k = 0,0,0

        while (i < len(left)) and (j < len(right)):
            if (left[i] < right[j]):
                data[k] = left[i]
                i += 1
            else:
                data[k] = right[j]
                j += 1
            k += 1
        
        while (i < len(left)):
            data[k] = left[i]
            i += 1
            k += 1
        while (j < len(right)):
            data[k] = right[j]
            j += 1
            k += 1

data = [45,11,2,3,4,-99,-31,5,4,1,0,-330,26,65,459,756,-123,45,-12,23,453,666,219,2]
print(data)
merge_sort(data)
print(data)         