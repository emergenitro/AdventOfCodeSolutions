import os

count = 0
with open(os.getcwd() + "\input.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        line = line.replace("\n", "").split(",")
        line[0], line[1] = line[0].split("-"), line[1].split("-")
        result = all(
            i in [i for i in range(int(line[0][0]), int(line[0][1]) + 1)]
            for i in [i for i in range(int(line[1][0]), int(line[1][1]) + 1)]
        )
        result1 = all(
            i in [i for i in range(int(line[1][0]), int(line[1][1]) + 1)]
            for i in [i for i in range(int(line[0][0]), int(line[0][1]) + 1)]
        )
        if result or result1:
            count += 1
print(count)
