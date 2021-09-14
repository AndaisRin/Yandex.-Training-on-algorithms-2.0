import statistics

n = int(input())
num = list(map(int, input().split()))
print(int(statistics.median(num)))
