import sys
n=int(input())
arr1=list(map(int,sys.stdin.readline().rstrip().split()))
arr2=list(map(int,sys.stdin.readline().rstrip().split()))
result=0
sortedArr=list(reversed(sorted(arr2)))
arr1=sorted(arr1)
for i in range(len(arr2)):
    result += sortedArr[i] * arr1[i]

print(result)