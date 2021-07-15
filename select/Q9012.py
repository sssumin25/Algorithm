import sys

itr = int(input())
answer = list()
for i in range(itr):
    tmpStr = sys.stdin.readline().rstrip()
    tmpList = list(tmpStr)
    tmpStack= list()
    topIdx = -1

    for j in range(len(tmpList)):
        if len(tmpStack) == 0:
            tmpStack.append(tmpList[j])
            topIdx += 1
        else:

            if tmpStack[topIdx] == '('and tmpList[j] ==')':
                tmpStack.pop()
                topIdx -= 1
            else:
                
                tmpStack.append(tmpList[j])
                topIdx += 1
    
    if len(tmpStack) == 0:
        answer.append('YES')
    else:
        answer.append('NO')

for i in range(itr):
    print(answer[i])