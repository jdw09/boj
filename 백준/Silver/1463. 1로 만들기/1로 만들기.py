n = int(input())
arr = [0] * (n)
index = [i for i in range(1, n+1)]

for i in range(1, n):
    arr[i] = arr[i-1] + 1

    if index[i] % 2 == 0:
        arr[i] = min(arr[i], arr[index[i] // 2 - 1] + 1)
    if index[i] % 3 == 0:
        arr[i] = min(arr[i], arr[index[i] // 3 - 1] + 1)

print(arr[n-1])