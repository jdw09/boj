from sys import stdin
from collections import deque
arrL = deque(stdin.readline().rstrip())
arrR = deque()

for _ in range(int(stdin.readline().rstrip())):
    cmd = stdin.readline().strip() #명령어 입력
    if cmd[0] == "P": #만약 P라면
        cmd, n = cmd.split() #숫자 분리
        arrL.append(n) #추가
    elif cmd == "L": #L이면
        if arrL: #arrL리스트가 공백이 아니라면
            arrR.append(arrL.pop()) #arrL의 맨 뒷 인덱스를 arrR에 추가
            arrR.rotate(1) #맨 뒷 인덱스를 맨 앞으로 추가
    elif cmd == "D": #만약 D라면
        if arrR: #arrR이 공백이 아니라면
            arrL.append(arrR.popleft()) #arrL에 arrR의 첫번째 인덱스를 추출해서 추가
    elif cmd == "B": #B면
        if arrL:
            arrL.pop() #arrL의 가장 오른쪽 인덱스 삭제
print("".join(arrL)+"".join(arrR))