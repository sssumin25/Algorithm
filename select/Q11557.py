import sys

case = int(input())

answer = []
for i in range(case):
    itr = int(input())
    tmpdic = {}
    for j in range(itr):
        name, drink = sys.stdin.readline().split()
        tmpdic[name] = int(drink)

    list_school = list(tmpdic.keys())
    list_drink = list(tmpdic.values())
    tmp = max(list_drink)   

    for j in list_school:
        if tmp == tmpdic.get(j):
            answer.append(j)
            break


for i in range(case):
    print(answer[i])