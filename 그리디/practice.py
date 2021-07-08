import sys

data = list(map(int, sys.stdin.readline().rstrip().split()))
data.sort()
print(data)
