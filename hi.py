import sys
a= int(sys.stdin.readline())
for i in range(a,-1,-1):
    print(' '*(a-i) + '*' *(i*2-1))
