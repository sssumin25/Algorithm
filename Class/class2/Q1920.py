# 1차 수정. input(), print() sys라이브러리 이용해서 수정함. --> 시간초과 
# import sys
# num = int(input())
# list_origin = list(map(int, sys.stdin.readline().split()))
# itr = int(input())
# list_count = list(map(int,sys.stdin.readline().split()))

# list_ans = []
# for i in range(itr):
#     if list_origin.count(list_count[i]) > 0:
#         list_ans.append(1)
#     else:
#         list_ans.append(list_origin.count(list_count[i]))

# for i in list_ans:
#     sys.stdout.write(str(i)+'\n')