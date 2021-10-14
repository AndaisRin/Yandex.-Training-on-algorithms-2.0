l = list(map(int, input().split()))
s = set()
for i in range(len(l)):
    if l[i] not in s:
        s.add(l[i])
        print('NO')
    else:
        print('YES')
