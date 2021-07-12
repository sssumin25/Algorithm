arr = []
for i in range(9):
    arr.append(int(input()))
 
max = max(arr)
print(max)
idx = arr.index(max)
print(idx+1)


#내가 원래 쓴 코드
#뭐가 틀렸는지 모르겠다.
# import sys 

# data = [0, 0, 0, 0, 0, 0, 0, 0, 0]

# for i in range(9):
#     data[i] = int(sys.stdin.readline().rstrip())

# print(data)
# max = data[0]
# idx = 0

# for i in range(9):
#     if max <= data[i]:
#         max = data[i]
#         idx = i

# print(max)
# print(idx+1)
