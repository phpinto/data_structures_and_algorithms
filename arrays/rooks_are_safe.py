def rooks_are_safe(chess_board):
    row_set, col_set = set(), set()
    for i in range(len(chess_board)):
        for j in range(len(chess_board[0])):
            if chess_board[i][j] == 1:
                if (i in row_set) or (j in col_set):
                    return False
                row_set.add(i)
                col_set.add(j)
    return True

arr1 = [[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,0,0]]
print(rooks_are_safe(arr1))
arr1 = [[1,0,0,0],[1,1,0,0],[0,0,0,1],[0,0,0,0]]
print(rooks_are_safe(arr1))
arr1 = [[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]]
print(rooks_are_safe(arr1))
arr1 = [[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,1]]
print(rooks_are_safe(arr1))