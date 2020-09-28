def insertion_sort(data):
    for i in range(1,len(data)):
        curr = data[i]
        j = i - 1
        while((curr < data[j]) and (j >= 0)):
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = curr

        

data = [45,11,2,3,4,99,31,5,4,1,0,0,26,65,459,756,123,45,12,23,453,666,219,2]
print(data)
insertion_sort(data)
print(data)