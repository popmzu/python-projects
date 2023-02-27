import random
randomList = []
for i in range (0, 10):
    n = random.randint(10, 50)
    randomList.append(n)
print(randomList)

for i in range (0, 10):
    if randomList[i]%2 == 0:
        print(randomList[i])

        