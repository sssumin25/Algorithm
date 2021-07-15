import sys

tmpStack = list()
answer = list()
cnt = 0
itr = int(input())

for i in range(itr):
    tmpList = list(sys.stdin.readline().split())
    if len(tmpList) == 2:
        tmpStack.append(int(tmpList[1]))
        cnt += 1
    else:
        if tmpList[0] == 'pop':
            if cnt == 0:
                answer.append(-1)
            else:
                answer.append(tmpStack.pop())
                cnt -= 1
        elif tmpList[0] == 'size':
            answer.append(cnt)
        elif tmpList[0] == 'empty':
            if cnt == 0:
                answer.append(1)
            else:
                answer.append(0)
        else: # 'top'
            if cnt == 0:
                answer.append(-1)
            else:
                answer.append(tmpStack[cnt-1])

for i in range(len(answer)):
    print(answer[i])
            
