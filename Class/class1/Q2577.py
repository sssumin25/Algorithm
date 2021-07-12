a= int(input())
b= int(input())
c= int(input())

ans = str(a*b*c)
tmp = [0,0,0,0,0,0,0,0,0,0]
for i in range(len(ans)):
    tmp[int(ans[i])] +=1


for i in range(10):
    print(tmp[i])


# result = list(str(a * b * c))
# for i in range(10):
#     print(result.count(str(i))) // count 함수 
