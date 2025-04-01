n,m=map(int,input().split())
arr=[_ for _ in range(2,int(n+1))]
cnt=0

for _ in range(m): #m만큼 반복
    p=arr[0] #p=min(arr)
    for i in arr: #arr 반복
        if not i%p: #나누어 떨어지면
            cnt+=1 #cnt++
            if cnt==m: #만약 m번째 수라면
                print(i) #출력
                exit() #종료
            arr.remove(i) #아니면 삭제
