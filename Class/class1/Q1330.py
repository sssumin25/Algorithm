a, b = map(int, input().split())

if a>b:
    print('>')
elif a == b:
    print('==') #등호 2개인데 하나만 써서 틀렸었음.
else:
    print('<')