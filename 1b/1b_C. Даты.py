num = list(map(int, input().split()))
x, y, z = num[0], num[1], num[2]
print(1) if (x > 12 or y > 12 or x == y) else print(0)
