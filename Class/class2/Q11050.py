import sys

n, k = map(int, sys.stdin.readline().split())

ans = 1
if n-k <k:
    k = n-k

# for i in range(N, N-K, -1):
# for문 형식 바꿔 쓸 수 있음. 
#     up *= i

for i in range(k):
    ans *= n
    n -= 1
for j in range(k):
    ans = ans/k
    k -=1

print(int(ans))