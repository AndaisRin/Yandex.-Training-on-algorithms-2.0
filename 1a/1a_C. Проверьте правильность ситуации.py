board = []
for i in range(3):
    string = list(map(int, input().split()))
    board.append(string)
k, t = [0, 0, 0], [False, False, False]
res = True
for i in range(3):
    for j in range(3):
        k[board[i][j]] += 1
for i in range(3):
    if board[i][0] == board[i][1] and board[i][1] == board[i][2]:
        t[board[i][1]] = True
    if board[0][i] == board[1][i] and board[1][i] == board[2][i]:
        t[board[1][i]] = True
if (k[1] - k[2] > 1) or (k[1] - k[2] < 0):
    res = False
if t[1] and (t[2] or (k[1] == k[2])):
    res = False
if (board[0][0] == board[1][1] == board[2][2] == 2 or board[0][2] == board[1][1] == board[2][0] == 2) and k[1] > k[2]:
    res = False
if (board[0][0] == board[1][1] == board[2][2] == 1 or board[0][2] == board[1][1] == board[2][0] == 1) and k[2] >= k[1]:
    res = False
print('YES') if res else print('NO')
