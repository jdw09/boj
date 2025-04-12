from sys import stdin

for _ in range(int(stdin.readline())): #테스트케이스만큼 반복
    a, b = map(int, stdin.readline().rstrip().split()) #행열 입력
    dc = {} #딕셔너리 선언(위치 저장용)

    for i in range(a): #행만큼 반복
        arr = list(map(int, stdin.readline().rstrip().split())) #열 입력받기
        for j in range(len(arr)): #열만큼 반복
            if arr[j] != -1: #만약 -1(빈칸)이 아니라면
                dc[arr[j]] = (i + 1, j + 1) #딕셔너리에 번호와 좌표 저장
    arr2 = sorted(dc.items()) #arr2 정렬

    # print(arr2) # 번호, 좌표 조합 리스트

    hh = [1] * (a + 1) #2차원 배열 생성
    result = 0 #결과 변수 선언

    for i, j in arr2: #arr2 선회 i : 차량번호, j: 좌표
        result += abs(1 - j[0]) * 20 #행 움직이는 만큼 초 추가(왕복이라 20초)
        result += min(abs(hh[j[0]] - j[1]), abs(b - abs(hh[j[0]] - j[1]))) * 5
        hh[j[0]] = j[1]
    print(result)