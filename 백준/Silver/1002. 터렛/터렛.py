import math

n=int(input())


for _ in range(n):
    tr=list(map(int,input().split()))
    t1,t2=tr[:3],tr[3:]

    distance=math.sqrt((t1[0]-t2[0])**2 + (t1[1]-t2[1])**2)
    if distance==0 and t1[-1] == t2[-1]:
        print(-1)
    elif distance == t1[-1] + t2[-1] or distance == abs(t1[-1] - t2[-1]):
        print(1)
    elif abs(t1[-1] - t2[-1]) < distance < t1[-1] + t2[-1]:
        print(2)
    else:
        print(0)