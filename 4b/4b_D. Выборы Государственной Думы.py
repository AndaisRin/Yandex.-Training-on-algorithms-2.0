names, votes = list(), list()
sumVotes = 0
data = open('input.txt')
for line in data:
    line = line.split()
    partyName = ' '.join(line[:-1])
    partyVotes = int(line[-1])
    names.append(partyName)
    votes.append(partyVotes)
    sumVotes += partyVotes
mandates, patry_part = list(), list()
sum_mandates = 0
for i in range(len(names)):
    partyMandates = (votes[i] * 450) / sumVotes
    sum_mandates += int(partyMandates)
    mandates.append(int(partyMandates))
    patry_part.append(partyMandates - int(partyMandates))
while sum_mandates < 450:
    i = 0
    for j in range(1, len(patry_part)):
        if ((patry_part[j] > patry_part[i]) or (
                patry_part[j] == patry_part[i] and votes[j] > votes[i])):
            i = j
    mandates[i] += 1
    sum_mandates += 1
    patry_part[i] = 0
for k in range(len(names)):
    print(names[k], mandates[k])
