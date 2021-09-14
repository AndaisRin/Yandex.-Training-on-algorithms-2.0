d = int(input())
x = list(map(int, input().split()))
da = (x[0] ** 2 + x[1] ** 2) ** 0.5
db = ((x[0] - d) ** 2 + x[1] ** 2) ** 0.5
dc = (x[0] ** 2 + (x[1] - d) ** 2) ** 0.5
if x[0] >= 0 and x[1] >= 0 and x[0] + x[1] <= d:
    print(0)
else:
    if da <= db:
        print(1) if da <= dc else print(3)
    else:
        print(2) if db <= dc else print(3)
