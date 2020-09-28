def bubble_sort(data):
    for i in range(len(data) - 1):
        for j in range(len(data) - i - 1):
            if data[j] > data[j + 1]:
                temp = data [j + 1]
                data[j + 1] = data[j]
                data[j] = temp

data = [45,11,2,3,4,99,31,5,4,1,0,0,26,65,459,756,123,45,12,23,453,666,219,2]
print(data)
bubble_sort(data)
print(data)