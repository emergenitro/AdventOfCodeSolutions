import os
totalSum = 0
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Part 1
# with open(os.getcwd()+"\input.txt", "r") as f:
#     lines = f.readlines()
#     for line in lines:
#         firstcompartement, secondcompartement = line[:len(line)//2], line[len(line)//2:]
#         commonletters = ''.join(set(firstcompartement).intersection(secondcompartement))
#         for i in commonletters: totalSum += letters.index(i)+1
# print(totalSum)

# Part 2
with open(os.getcwd() + "\input.txt", "r") as f:
    lines = f.readlines()
    for i in range(0, len(lines), 3):
        tempList = [lines[j].replace('\n', '') for j in range(i, i+3)]
        for j in list(set.intersection(*map(set, tempList))):
            totalSum += letters.index(j)+1
print(totalSum)
