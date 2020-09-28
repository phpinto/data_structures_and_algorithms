def quick_sort(data, first, last):
    if first < last:
        pivot_index = partition(data, first, last)

        quick_sort(data, first, pivot_index - 1)
        quick_sort(data, pivot_index + 1, last)
    
def partition(data, first, last):
    pivot = data[first]
    p1 = first + 1
    p2 = last
    while (True):
        while (p1 <= p2) and (data[p1] <= pivot):
            p1 += 1
        while (p1 <= p2) and (data[p2] >= pivot):
            p2 -= 1
        if p1 > p2:
            break
        else:
            data[p1], data[p2] = data[p2], data[p1]
    data[first], data[p2] = data[p2], pivot
    
    return p2

data = [45,11,2,3,4,99,31,5,4,1,0,0,26,65,459,756,123,45,12,23,453,666,219,2]
print(data)
quick_sort(data,0,len(data)-1)
print(data)