import os

# Part 1
# with open(os.getcwd() + "\input.txt", "r") as f:
#     data = f.readlines()
# tempSum = 0
# maxSum = 0
# for i in data:
#     if i == '\n':
#         if maxSum < tempSum:
#             maxSum = tempSum
#         tempSum = 0
#     else:
#         tempSum += int(i)
# print(maxSum)

# Part 2
with open(os.getcwd() + "\input.txt", "r") as f:
    data = f.readlines()
tempSum = 0
sumList = []
for i in data:
    if i == '\n':
        sumList.append(tempSum)
        tempSum = 0
    else:
        tempSum += int(i)
sumList.sort(reverse=True)
print(sum(sumList[:3]))
