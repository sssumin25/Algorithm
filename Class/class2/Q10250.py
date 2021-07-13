import sys

itr = int(input())
ans = []

for i in range(itr):
    a, b, c = map(int, sys.stdin.readline().split())
    tmp = c%a

    if tmp == 0:
        tmpN = '%d%02d'%(a, c/a)
        ans.append(int(tmpN))
    else:
        tmpN = '%d%02d'%(c%a, (c/a)+1)
        ans.append(int(tmpN))

for i in ans:
    print(i)

