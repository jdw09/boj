status = None
melodies = list(map(int, input().split()))

for index in range(7):
    if (melodies[index] + 1 == melodies[index + 1]):
        if (status == None):
            status = "ascending"
        elif (status != "ascending"):
            status = "mixed"
    elif (melodies[index] == melodies[index + 1] + 1):
        if (status == None):
            status = "descending"
        elif (status != "descending"):
            status = "mixed"
    else:
        status = "mixed"

print(status)