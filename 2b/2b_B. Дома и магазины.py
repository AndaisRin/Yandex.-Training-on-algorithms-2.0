builds = list(map(int, input().split()))
shops = [i for i, x in enumerate(builds) if x == 2]
houses = [i for i, x in enumerate(builds) if x == 1]
distance = []
for h in houses:
    maximum = 10
    for s in shops:
        r = abs(h - s)
        if r < maximum:
            maximum = r
    distance.append(maximum)
print(max(distance))
