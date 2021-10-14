l = list(map(int, input().split()))
s = dict()
for i in range(len(l)):
    if l[i] not in s.keys():
        s[l[i]] = 1
    else:
        s[l[i]] = s[l[i]] + 1
for k, v in s.items():
    if v == 1:
        print(k, end=' ')
