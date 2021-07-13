itr = int(input())
list =[]
for i in range(itr):
    list.append(int(input()))

list.sort()

for i in range(itr):
    print(list[i])

#input()과 print()를 사용하지 않는다면
# import sys
# n = int(input())
# l = []
# for i in range(n):
#     l.append(int(sys.stdin.readline()))
# for i in sorted(l):
#     sys.stdout.write(str(i)+'\n')