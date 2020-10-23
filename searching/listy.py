class Listy(object):
    def __init__(self, data=[]):
        self.data = data

    def elementAt(self,i):
        if i >= len(self.data):
            return -1
        return self.data[i]

    def __str__(self):
        print(self.data)


def listy_binary_search(listy, start, end, item):
    while end >= start:
        mid_point = (end + start)//2
        element = listy.elementAt(mid_point)
        if element == item:
            return mid_point
        if (element > item or element == -1):
            end = mid_point - 1
        else:
            start = mid_point + 1
    return -1

def find_element(listy, item):

    end = 1
    while (listy.elementAt(end) != -1 and listy.elementAt(end) <= item):
        if listy.elementAt(end) == item:
            return end
        end *= 2

    return listy_binary_search(listy, (end / 2), end, item)


listy = Listy([1,2,4,6,9,11,14,21,24,55,78,210,311,450,1000,1220, 4500, 130000, 280556])
print(find_element(listy,9))
print(find_element(listy,24))
print(find_element(listy,2))
print(find_element(listy,11))
print(find_element(listy,14))
print(find_element(listy,78))
print(find_element(listy,311))
print(find_element(listy,1000))
print(find_element(listy,1220))
print(find_element(listy,4500))
print(find_element(listy,130000))
print(find_element(listy,280556))
print(find_element(listy,-360))
print(find_element(listy,3))
print(find_element(listy,288))
print(find_element(listy,-450))
print(find_element(listy,1100))
print(find_element(listy,1300))