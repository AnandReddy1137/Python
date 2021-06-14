def evaluate_new(A, r, c, L ,H):
    if r < 0 or r >= L or c < 0 or c >= H:
        return 0
    else:
        return A[r][c]


def get_max_length(A, r, c, L, H, size):
    global cntarr
    global max_size
    if r < 0 or r >= L or c < 0 or c >= H:
        return
    cntarr[r][c] = 1
    size = size + 1
    if size > max_size:
        max_size = size
    directions = [[-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0]]
    for i in range(0, 8):
        newi = r + directions[i][0]
        newj = c + directions[i][1]
        val = evaluate_new(A, newi, newj,L,H)
        if val > 0 and cntarr[newi][newj] == 0:
            get_max_length(A, newi, newj, L, H, size)
    cntarr[r][c] = 0


def find_max_ones(A, rmax, colmax):
    global max_size
    global size
    global cntarr
    for i in range(0, rmax):
        for j in range(0, colmax):
            if A[i][j] == 1:
                get_max_length(A, i, j, rmax, colmax, 0)
    return max_size


z = [[1, 0, 1], [0, 1, 1], [1, 0, 1]]
rmax = 3
colmax = 3
size = 0
cntarr = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in z:
    print(i)

max_size = 0
print(find_max_ones(z, rmax, colmax))
