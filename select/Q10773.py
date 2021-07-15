itr = int(input())

answer = list()
for i in range(itr):
    tmpN = int(input())

    if tmpN == 0:
        answer.pop()
    else:
        answer.append(tmpN)

print(sum(answer))