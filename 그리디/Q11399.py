import sys

iter = int(input())
data = list(map(int, sys.stdin.readline().rstrip().split())) #입력을 받는다.
data.sort() #오름차순으로 정렬, 작을수록 많이 더해지도록

result = 0
for i in range(iter):
    result += (i+1)*data[(iter-1-i)]
print(result)