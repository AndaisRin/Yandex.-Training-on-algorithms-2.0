l, k = map(int, input().split())
legs = list(map(int, input().split()))
new_legs = []
if l % 2 != 0 and (l // 2 in legs):
    print(l // 2)
else:
    for i1 in range(l // 2 - 1, -1, -1):
        if i1 in legs:
            new_legs.append(i1)
            break
    for i2 in range(l // 2, l, 1):
        if i2 in legs:
            new_legs.append(i2)
            break
print(*new_legs)
