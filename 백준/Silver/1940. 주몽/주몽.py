n = int(input())
m = int(input())
cnt = 0
ingredent = list(map(int,input().split()))

for i in range(n-1):
    for j in range(i+1, n):
        if (ingredent[i] + ingredent[j]) == m and ingredent[i] != -1 and ingredent[j] != -1:
            cnt += 1
            ingredent[i], ingredent[j] = -1, -1
            break

print(cnt)