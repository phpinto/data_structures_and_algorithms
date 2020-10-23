def count_neighbors(board, row, col):
        # Terminating Condition
        if row >= len(board) or col >= len(board[0]) or row < 0 or col < 0 or board[row][col] != 0:
            return 0
        # Recursive Neighbor Visit
        size = 1
        board[row][col] = -1
        for new_row in range(-1,2):
            for new_col in range(-1,2):
                size += count_neighbors(board, row + new_row, col + new_col)
        return size

def pond_sizes(board):
    pond_sizes = []
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == 0:
                pond_sizes.append(count_neighbors(board, row, col))
    return pond_sizes

board = [[0,2,1,0],[0,1,0,1],[1,1,0,1],[0,1,0,1]]
print(pond_sizes(board))