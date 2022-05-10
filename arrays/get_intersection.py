def get_intersection(A, B):

    set_A = set(A)
    set_B = set(B)

    if len(set_A) < len(set_B):
        return [x for x in set_A if x in set_B]
    else:
        return [x for x in set_B if x in set_A]


print(get_intersection([1,2,3,4,5], [0,1,3,7]))
print(get_intersection([1,3,5,2,4], [7,1,3,0]))
print(get_intersection([5,6,2,0,11,14,9], [7,1,3,0,5]))
print(get_intersection([5,6,2,0,11,14,9], [9,1,3,0,5]))
print(get_intersection([1,3,5,2,4], [73,11,34,0,5]))