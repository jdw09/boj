arr = []
for _ in range(9):
    arr.append(int(input()))

max_number = max(arr)
max_index = arr.index(max_number) + 1

print(max_number)
print(max_index)