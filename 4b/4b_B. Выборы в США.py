votes = dict()
data = open('input.txt', 'r', encoding='utf8')
for line in data:
    vote = line.split()
    votes[vote[0]] = votes.get(vote[0], 0) + int(vote[1])
for name, val in sorted(votes.items()):
    print(name, val)
