itr = int(input())

answer = []
for i in range(itr):
    a , b = map(int, input().split())
    result = a+b
    answer.append(result)

for i in range(itr):
    print(answer[i])

