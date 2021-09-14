num = list(map(int, input().split()))
quantity, first, second = num[0], num[1], num[2]
if first > second:
    first, second = second, first
way_there = abs(second - first - 1)
way_back = abs(quantity - second + first - 1)
print(min(way_back, way_there))
