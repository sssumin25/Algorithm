import sys

tmpdic ={}
data = sys.stdin.readline().rstrip().split()
tmplist = list(data[0].upper())

for i in tmplist:
    try:
        tmpdic[i] += 1
    except:
        tmpdic[i] = 1

answer = [k for k,v in tmpdic.items() if max(tmpdic.values()) == v] #표현식 --> 딕셔너리 라이브러리? 

if len(answer) !=  1:
    print('?')
else:
    print(answer[0])