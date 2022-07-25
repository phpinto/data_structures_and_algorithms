import time

# Brute Force:
 
def find_peak_elements(arr):

    for i in range(len(arr)):
        if (i == 0 or arr[i - 1] < arr[i]) and (i == (len(arr) - 1) or arr[i] > arr[i + 1]):
            return i


def find_peak_elements2(arr):
    p1 = 0
    p2 = len(arr) - 1
    while p1 < p2:
        if (p1 == 0 or arr[p1 - 1] < arr[p1]) and arr[p1] > arr[p1 + 1]:
            return p1
        if (arr[p2 - 1] < arr[p2]) and (p2 == (len(arr) - 1) or arr[p2] > arr[p2+ 1]):
            return p2
        p1 += 1
        p2 -= 1

    return False

start_time = time.time()
print("Peak Index: " + str(find_peak_elements([1,2,3,4,5,6,7,88,8,10,11,12,15,16,15,14,13,10,9,7,5,2,1,0])))
print("--- %s seconds ---" % (time.time() - start_time))
print()
start_time = time.time()
print("Peak Index: " + str(find_peak_elements2([1,2,3,4,5,6,7,8,8,8,10,11,12,15,16,15,14,13,10,9,7,5,2,1,0])))
print("--- %s seconds ---" % (time.time() - start_time))


# Optimized

def find_peak_elements_rec(arr, l, r):

    while True:
        mid = (l + r) // 2
        if (mid == 0 or arr[mid - 1] < arr[mid]) and (mid == ((len(arr) - 1)) or arr[mid] > arr[mid + 1]):
            return mid

        elif arr[mid + 1] > arr[mid]:
            l = mid + 1

        else:
            r = mid

print()
arr = [1,2,3,4,5,6,7,8,8,8,10,11,12,15,16,15,14,13,10,9,7,5,2,1,0]
start_time = time.time()
print("Peak Index: " + str(find_peak_elements_rec(arr, 0, len(arr))))
print("--- %s seconds ---" % (time.time() - start_time))
arr = list(range(22))
start_time = time.time()
print("Peak Index: " + str(find_peak_elements_rec(arr, 0, len(arr))))
print("--- %s seconds ---" % (time.time() - start_time))

