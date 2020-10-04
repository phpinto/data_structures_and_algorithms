def find_item(item, ordered_list):
    # Implementing Binary Search:

    start = 0
    end = len(ordered_list) - 1
    while end >= start:
        mid_point = (start + end) // 2
        if ordered_list[mid_point] == item: 
            while mid_point > 0:
                if ordered_list[mid_point - 1] == item:
                    mid_point -= 1
                else: 
                    break
            return mid_point
        elif ordered_list[mid_point] > item: 
            end = mid_point - 1
        else:
            start = mid_point + 1
    return None

def find_item_recursive(item, ordered_list, start=0, end=None):
    # Implementing Recursive Binary Search:

    if end is None:
        end = len(ordered_list) - 1
    if end < start:
        return None
    mid_point = (start + end) // 2
    if ordered_list[mid_point] == item: 
        while mid_point > 0:
            if ordered_list[mid_point - 1] == item:
                mid_point -= 1
            else: 
                break
        return mid_point
    elif ordered_list[mid_point] > item: 
        end = mid_point - 1
        return find_item_recursive(item, ordered_list, start, end)
    else:
        start = mid_point + 1
        return find_item_recursive(item, ordered_list, start, end)


data = sorted([45,11,2,3,4,99,31,5,4,1,0,0,26,65,459,756,123,45,12,23,453,666,219,2])
print(data)
print(find_item(453,data))
print(find_item(31,data))
print(find_item(0,data))
print(find_item(-13,data))
print(find_item(9999,data))
print(find_item(2,data))
print(find_item(756,data))
print(data)
print(find_item_recursive(453,data))
print(find_item_recursive(31,data))
print(find_item_recursive(0,data))
print(find_item_recursive(-13,data))
print(find_item_recursive(9999,data))
print(find_item_recursive(2,data))
print(find_item_recursive(756,data))