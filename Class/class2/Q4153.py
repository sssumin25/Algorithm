import sys
ans = []

while True:
    data = list(map(int, sys.stdin.readline().split()))
    if data[0]== 0 and data[1]== 0 and data[2] == 0:
        break
    else:
        data.sort()
        if (data[0]**2+data[1]**2 == data[2]**2):
            ans.append('right')
        else:
            ans.append('wrong')

for i in ans:
    print(i)
