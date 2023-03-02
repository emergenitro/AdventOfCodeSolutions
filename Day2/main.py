import os
totalScore = 0

# Part 1
# with open(os.getcwd() + "\input.txt") as f:
#     lines = f.readlines()
#     for line in lines:
#         score = 0
#         line = line.split(" ")
#         line[1] = line[1].replace("\n", "")
#         if line[1] == 'X': score += 1
#         if line[1] == 'Y': score += 2
#         if line[1] == 'Z': score += 3
#         if (line[1] == 'Y' and line[0] == 'A') or (line[1] == 'X' and line[0]=='C') or (line[1] == 'Z' and line[0] == 'B'): score += 6
#         elif (line[1] == 'X' and line[0] == 'A') or (line[1] == 'Z' and line[0]=='C') or (line[1] == 'Y' and line[0] == 'B'): score += 3
#         totalScore += score
# print(totalScore)

# Part 2
dictThing = {"A" : 1, "B" : 2, "C" : 3}
winnerLoser = {"A" : "B", "B" : "C", "C" : "A"}
loserWinner = {"A" : "C", "B" : "A", "C" : "B"}
with open(os.getcwd() + "\input.txt") as f:
    lines = f.readlines()
    for line in lines:
        score = 0
        line = line.split(" ")
        line[1] = line[1].replace("\n", "")
        if (line[1] == 'X'):
            score += dictThing[loserWinner[line[0]]]
        if (line[1] == 'Y'): 
            score += 3
            score += dictThing[line[0]]
        if (line[1] == 'Z'): 
            score += 6
            score += dictThing[winnerLoser[line[0]]]
        print(line, score)
        totalScore += score
print(totalScore)