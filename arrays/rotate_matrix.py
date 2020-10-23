import copy

def rotate_matrix(matrix):
    n_rows = len(matrix)
    n_cols = len(matrix[0])

    #rotated_matrix = copy.deepcopy(matrix)
    rotated_matrix = [ [ 0 for i in range(n_rows) ] for j in range(n_cols) ]

    for row in range(n_rows):
        for col in range(n_cols):
            rotated_matrix[col][(n_rows - row - 1)] = matrix[row][col]

    return rotated_matrix

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
matrix_2 = [[1,2,3,4,96],[5,6,7,8,97],[9,10,11,12,98],[13,14,15,16,99]]
print(matrix)
print(rotate_matrix(matrix))
print(matrix_2)
print(rotate_matrix(matrix_2))