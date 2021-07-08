import math

data = int(input())

result = -1

if data % 5 == 0: #5의 배수이면 계산 결과 바로 출력
    result = data/5
    print(int(result))
else:
    five = math.floor(data/5)
    list = []
    for i in range(five+1): #5의 개수 기준으로
        tmp = data
        count = 0
        count += i
        tmp -= count*5 
        if tmp %3 == 0: #5kg 제외한 나머지가 나누어 떨어지면
            count += tmp/3
            list.append(count)
   
    if len(list) == 0: #3kg, 5kg으로 만들어질 수 없다면
        print(result)
    else:
        list.sort()
        print(int(list[0]))



# sugar = int(input())

# bag = 0
# while sugar >= 0 :
#     if sugar % 5 == 0 :  # 5의 배수이면
#         bag += (sugar // 5)  # 5로 나눈 몫을 구해야 정수가 됨
#         print(bag)
#         break
#     sugar -= 3  
#     bag += 1  # 5의 배수가 될 때까지 설탕-3, 봉지+1
# else :
#     print(-1)