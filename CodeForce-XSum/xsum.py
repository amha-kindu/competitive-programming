

tc_num = int(input())
for _ in range(tc_num):
    n, m = list(map(int, input().split()))
    left_diag = {}
    right_diag = {}
    board = []
    for i in range(n):
        board_row = list(map(int, input().split()))
        for j in range(m):
            left_diag[i-j] = left_diag.get(i-j, 0) + board_row[j]
            right_diag[i+j] = right_diag.get(i+j, 0) + board_row[j]
        board.append(board_row)

    max_gain = -float('inf')
    for r in range(n):
        for s in range(m):
            gain = left_diag[r-s] + right_diag[r+s] - board[r][s]
            max_gain = max(max_gain, gain)
    print(max_gain)

    
