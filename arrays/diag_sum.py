def diag_sum(arr_2d):
    sum = 0
    for i in range(len(arr_2d[0])):
        sum += arr_2d[i][i]
    return (sum)

print(diag_sum([[1,2,3],[4,5,6],[7,8,9]]))
print(diag_sum([[0,2,3],[4,0,6],[7,8,0]]))
print(diag_sum([[45,2,3,6],[4,-45,6,9],[7,9,45,11],[9,8,4,-45]]))
print(diag_sum([[3,2,3,6],[4,4,6,9],[7,45,11,11],[9,8,4,2]]))