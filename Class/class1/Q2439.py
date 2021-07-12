import sys

num = int(sys.stdin.readline().rstrip())

for i in range(num):
    for j in range(num):

        if j < (num- i-1):
            print(' ', end='')
        else:
            print('*', end='')
    print('\n', end='')