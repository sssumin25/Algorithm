import sys

data = list(map(int, sys.stdin.readline().rstrip().split()))

sum = 0

for i in range(len(data)):
   sum += (data[i]**2)

answer = sum %10

print(answer)