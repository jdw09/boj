import sys
arr=[]
for _ in range(int(input())):
    arr.append(list(sys.stdin.readline().strip().split()))
arr.sort(key=lambda x:(-int(x[1]), int(x[2]),-int(x[3]),x[0]))
for i in arr:
    print(i[0])
