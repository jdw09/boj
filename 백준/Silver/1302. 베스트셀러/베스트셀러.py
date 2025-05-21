n=int(input())
name=[]
cnt=[1 for _ in range(n)]

for i in range(n):
    user=input()
    if user in name:
        cnt[name.index(user)] += 1
        continue
    name.append(user)


for i in range(len(name)-1):
    for j in range(i, len(name)):
        if name[i] > name[j]:
            name[i],  name[j] = name[j], name[i]
            cnt[i], cnt[j] = cnt[j], cnt[i]

print(name[cnt.index(max(cnt))])