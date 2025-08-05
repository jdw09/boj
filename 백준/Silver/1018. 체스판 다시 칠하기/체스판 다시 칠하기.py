n,m=map(int,input().split()) #가로 세로 입력
chess=[input() for _ in range(n)] #체스판 입력

w_board = [
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW"
] #정답지(흰)
b_board = [
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB"
]#정답지(흑)

def check(i,j):#수정할 부분 체크용 함수
    result_w=0
    result_b=0
    for di in range(8): #8*8로 나눠서 확인하기 때문에
        for dj in range(8):
            ni=di+i #ni,nj = now i, now j
            nj=dj+j
            if w_board[di][dj] != chess[ni][nj]: #만약 정답지와 다르다면
                result_w += 1
            if b_board[di][dj] != chess[ni][nj]:
                result_b += 1
    return min(result_b,result_w) #더 작게 수정할 것을 리턴

result = 3000 #result : 최대 출력값 이상으로 해둠

for i in range(n-7): #out of range 예방용 -7까지 반복(함수 내에서 8씩 반복하기 때문)
    for j in range(m-7):
        result=min(check(i,j), result) #result와 함수 결과값 중 더 적은 것을 result로

print(result) #출력