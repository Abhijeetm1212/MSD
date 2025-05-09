def issafe(arr, x, y, n):
    # Check the same column
    for row in range(x):
        if arr[row][y] == 1:
            return False

    # Check upper-left diagonal
    row, col = x, y
    while row >= 0 and col >= 0:
        if arr[row][col] == 1:
            return False
        row -= 1
        col -= 1

    # Check upper-right diagonal
    row, col = x, y
    while row >= 0 and col < n:
        if arr[row][col] == 1:
            return False
        row -= 1
        col += 1

    return True

def nQueen(arr, x, n):
    if x >= n:
        return True  # All queens placed successfully

    for col in range(n):
        if issafe(arr, x, col, n):
            arr[x][col] = 1  # Place queen
            if nQueen(arr, x + 1, n):
                return True
            arr[x][col] = 0  # Backtrack

    return False  # No position is safe in this row

def main():
    n = int(input("Enter number of Queens: "))
    arr = [[0] * n for _ in range(n)]

    if nQueen(arr, 0, n):
        print("One possible solution:")
        for row in arr:
            print(" ".join(str(cell) for cell in row))
    else:
        print("No solution exists for", n, "Queens.")

if __name__ == '__main__':
    main()
