word = str(input())
symbols = []
for j in word:
    symbols.append(j)
money = 0
for i in range(0, (len(symbols) // 2)):
    if symbols[i] != symbols[-1 - i]:
        money += 1
print(money)
