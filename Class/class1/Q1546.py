import sys

num = int(sys.stdin.readline().rstrip())
data = list(map(int, sys.stdin.readline().rstrip().split()))

maxN = max(data)

sum = 0
for i in data:
    sum += i/maxN*100
        

answer = sum/num

print(answer)
