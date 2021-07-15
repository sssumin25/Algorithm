import sys

answer = list()
while True:
    tmpList = list(sys.stdin.readline().rstrip())
    
    if len(tmpList) == 1 and tmpList[0] =='.': break
    
    filteredList = [x for x in tmpList if x =='(' or x == ')' or x== '['or x == ']']
    
    tmpStack= list()
    topIdx = -1

    for j in range(len(filteredList)):
        if len(tmpStack) == 0:
            tmpStack.append(filteredList[j])
            topIdx += 1
        else:

            if tmpStack[topIdx] == '('and filteredList[j] ==')':
                tmpStack.pop()
                topIdx -= 1
            elif tmpStack[topIdx] == '[' and filteredList[j] == ']':
                tmpStack.pop()
                topIdx -= 1
            else:
                
                tmpStack.append(filteredList[j])
                topIdx += 1
    
    if len(tmpStack) == 0:
        answer.append('yes')
    else:
        answer.append('no')


for i in range(len(answer)):
    print(answer[i])

