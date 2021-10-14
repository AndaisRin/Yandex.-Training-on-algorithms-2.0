n = int(input())
all_possible = set(range(1, n + 1))
beatrice = input().split()
while beatrice[0] != 'HELP':
    beatrice = set(map(int, beatrice))
    august = input().split()
    if august[0] == 'YES':
        all_possible &= beatrice
    elif august[0] == 'NO':
        all_possible -= beatrice
    beatrice = input().split()
print(*sorted(all_possible))
