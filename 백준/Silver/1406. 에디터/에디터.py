from sys import stdin
from collections import deque
arrL = deque(stdin.readline().rstrip())
arrR = deque()

for _ in range(int(stdin.readline().rstrip())):
    cmd = stdin.readline().strip()
    if cmd[0] == "P":
        cmd, n = cmd.split()
        arrL.append(n)
    elif cmd == "L":
        if arrL:
            arrR.append(arrL.pop())
            arrR.rotate(1)
    elif cmd == "D":
        if arrR:
            arrL.append(arrR.popleft())
    elif cmd == "B":
        if arrL:
            arrL.pop()
print("".join(arrL)+"".join(arrR))