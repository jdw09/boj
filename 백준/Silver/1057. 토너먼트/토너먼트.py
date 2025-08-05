def find_cnt():
    n, kim, im = map(int, input().split())

    now_participant = [0 for _ in range(1, n + 1)]
    now_participant[kim - 1] = 1
    now_participant[im - 1] = 1

    next_participant = []


    cnt = 1
    while True:
        is_walkover = False

        if (len(now_participant) % 2 != 0):
            next_participant.append(now_participant[-1])
            now_participant.pop()
            is_walkover = True
        
        for i in range(0, (len(now_participant)), 2):

            if (now_participant[i] and now_participant[i + 1]):
                return cnt

            if (now_participant[i] or now_participant[i + 1]):
                next_participant.append(1)

            else:
                next_participant.append(0)

        cnt += 1

        if is_walkover:
            next_participant.append(next_participant[0])
            next_participant.pop(0)

        now_participant = next_participant
        next_participant = []

result = find_cnt()

print(result)