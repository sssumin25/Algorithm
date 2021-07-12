num = int(input())

tmp = list(input().split())

ans = map(int, tmp)
print(min(ans), end = ' ')
ans = map(int, tmp) #여기를 왜 한번 더 해줘야 max가 제대로 실행되는지
                    #이 코드 없으면 ValueError: max() arg is an empty sequence 에러가 나옴.
print(max(ans))
