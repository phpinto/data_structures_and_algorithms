def find_item(item, unordered_list):
        for i in range(len(unordered_list)):
            if unordered_list[i] == item: return i
        return str(item) + " is not on the list."

data = [45,11,2,3,4,99,31,5,4,1,0,0,26,65,459,756,123,45,12,23,453,666,219,2]
print(find_item(453,data))
print(find_item(31,data))
print(find_item(0,data))
print(find_item(-13,data))
print(find_item(9999,data))