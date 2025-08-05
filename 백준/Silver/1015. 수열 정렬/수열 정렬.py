def replace(index, prop):
    del arr_P[index]
    arr_P.insert(index, prop)
def make_minus(index):
    del arr_B[index]
    arr_B.insert(index, -1)

n = int(input())
arr_A = list(map(int,input().split()))
arr_B = sorted(arr_A)
arr_P = [0 for _ in range(n)]

for i in range(n):
    found_number = arr_B.index(arr_A[i])
    make_minus(found_number)
    replace(i, found_number)

print(" ".join(map(str, arr_P)))