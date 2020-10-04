def count_negatives_n2(board):
    count = 0
    ops = 0
    for row in board:
        for col in row:
            ops += 1
            if col < 0:
                count += 1
    print("Operations: " + str(ops))
    return count

arr1 = [[-4,-3,-1,1],[-2,-2,1,2],[-1,1,2,3],[1,2,4,5]]
arr2 = [[-4,-3,-1,-1],[-2,-2,-1,-2],[-1,-1,-2,-3],[-1,-2,-4,-5]]
arr3 = [[-4,-3,-1,-1],[-2,-2,-1,-2],[-1,-1,-2,-3],[1,2,4,5]]

print("O(N^2):")
print(count_negatives_n2(arr1))
print(count_negatives_n2(arr2))
print(count_negatives_n2(arr3))

def count_negatives_n2_better(board):
    rows, cols = len(board), len(board[0])
    i, count = 0, 0
    ops = 0
    while i < rows:
        j = 0
        while j < cols:
            ops += 1
            if board[i][j] < 0:
                count += 1
            else:
                cols -= 1
            j += 1
        i += 1
    print("Operations: " + str(ops))
    return count

print("O(N^2) slightly better:")
print(count_negatives_n2_better(arr1))
print(count_negatives_n2_better(arr2))
print(count_negatives_n2_better(arr3))

def count_negatives_n(board):
    rows = len(board)
    count = 0
    j = len(board[0]) - 1
    ops = 0
    for i in range(rows):
        while (j >= 0):
            ops += 1
            if board[i][j] < 0:
                count += (j + 1)
                break
            else:
                j -= 1
        if (j < 0):
            print("Operations: " + str(ops))
            return count
    print("Operations: " + str(ops))
    return count
    

print("O(N):")
print(count_negatives_n(arr1))
print(count_negatives_n(arr2))
print(count_negatives_n(arr3))