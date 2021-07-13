itr = int(input())

ans = []
for i in range(itr):
    tmp = list(map(int, input().split()))
    ans.append(tmp)

ans.sort()
for i in range(itr):
    print(str(ans[i][0])+" "+str(ans[i][1]))