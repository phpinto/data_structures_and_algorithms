def sorted_matrix_search(matrix, value):
    n_rows = len(matrix)
    row, col = 0, len(matrix[0]) - 1

    while (row < n_rows and col >= 0):

        if matrix[row][col] == value:
            return (row,col)
        if value > matrix[row][col]:
            row += 1
        else:
            col -= 1
    return -1


arr = [[15,20,40,85],[20,35,80,95],[30,55,95,105],[40,80,100,120]]

print(sorted_matrix_search(arr,95))
print(sorted_matrix_search(arr,20))
print(sorted_matrix_search(arr,80))
print(sorted_matrix_search(arr,15))
print(sorted_matrix_search(arr,120))
print(sorted_matrix_search(arr,35))