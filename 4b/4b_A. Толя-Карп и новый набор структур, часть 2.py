n = int(input())
s = dict()
for i in range(n):
    a, b = map(int, input().split())
    if a not in s.keys():
        s[a] = b
    else:
        s[a] = s[a] + b
list_k = list(s.keys())
list_k.sort()
for i in list_k:
    print(i, s[i])
