import sys

itr = int(input())
answer = [-1]*itr
data = list(map(int, sys.stdin.readline().rstrip().split()))

# 1. 아래와 같이 구현하면 O(N^2)의 시간복잡도가 걸릴 수 있음
# for i in range(itr):
    
#     for j in range(i+1, itr):
        
#         if data[i] < data[j]:
            
#             answer[i] = data[j]
#             break

#2. 이 문제는 무조건 스택을 활용하여야 함
#스택에 인덱스를 저장하는 방식
stack = []

stack.append(0)
for i in range(1, itr):
    while stack and data[stack[-1]] < data[i]: # 여기가 주요 부분
        answer[stack.pop()] = data[i]
    stack.append(i)

    

for i in range(itr):
    print(answer[i], end = ' ')    