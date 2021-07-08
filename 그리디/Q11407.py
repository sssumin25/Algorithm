import sys
n, v =  map(int, sys.stdin.readline().rstrip().split())
data =[]

for i in range(n):
    data.append(int(input()))

tmp = 0

for i in reversed(range(n)):
    if data[i] <= v:
        tmp = i
        break

count = 0
for i in reversed(range(tmp+1)):
    count += v//data[i]
    v %= data[i]

print(count)

# n, k = map(int, input().split())
# m = []
# num = 0
# for i in range(n):
#     m.append(int(input()))
# for i in range(n - 1, -1, -1):
#     if k == 0:
#         break
#     if m[i] > k:
#         continue
#     num += k // m[i]
#     k %= m[i]
# print(num)