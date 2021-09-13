def length(x1, y1, x2, y2):
    return (x2 - x1) ** 2 + (y2 - y1) ** 2


def are_equal_ab_cd_and_parallel(g):
    if (g[2] - g[0]) != 0 and (g[6] - g[4]) != 0:
        if length(g[0], g[1], g[2], g[3]) == length(g[4], g[5], g[6], g[7]) and \
                ((g[3] - g[1]) / (g[2] - g[0])) == ((g[7] - g[5]) / (g[6] - g[4])):
            return True
    else:
        if length(g[0], g[1], g[2], g[3]) == length(g[4], g[5], g[6], g[7]) and \
                abs(g[3] - g[1]) == abs(g[7] - g[5]):
            return True


def are_equal_ac_bd_and_parallel(g):
    if (g[4] - g[0]) != 0 and (g[6] - g[2]) != 0:
        if length(g[0], g[1], g[4], g[5]) == length(g[2], g[3], g[6], g[7]) and \
                ((g[5] - g[1]) / (g[4] - g[0])) == ((g[7] - g[3]) / (g[6] - g[2])):
            return True
    else:
        if length(g[0], g[1], g[4], g[5]) == length(g[2], g[3], g[6], g[7]) and \
                abs(g[5] - g[1]) == abs(g[7] - g[3]):
            return True


def are_equal_ad_bc_and_parallel(g):
    if (g[6] - g[0]) != 0 and (g[4] - g[2]) != 0:
        if length(g[0], g[1], g[6], g[7]) == length(g[2], g[3], g[4], g[5]) and \
                ((g[7] - g[1]) / (g[6] - g[0])) == ((g[5] - g[3]) / (g[4] - g[2])):
            return True
    else:
        if length(g[0], g[1], g[6], g[7]) == length(g[2], g[3], g[4], g[5]) and \
                abs(g[7] - g[1]) == abs(g[5] - g[3]):
            return True


def is_parallelogram(g):
    if (are_equal_ab_cd_and_parallel(g) and are_equal_ac_bd_and_parallel(g)) or \
            (are_equal_ab_cd_and_parallel(g) and are_equal_ad_bc_and_parallel(g)) or \
            (are_equal_ad_bc_and_parallel(g) and are_equal_ac_bd_and_parallel(g)):
        return True


def answer():
    grid = list(map(int, input().split()))
    print('YES') if is_parallelogram(grid) else print('NO')


m = int(input())
for i in range(m):
    answer()
