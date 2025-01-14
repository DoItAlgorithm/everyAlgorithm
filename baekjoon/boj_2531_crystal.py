N, d, k, c = map(int,input().split())
plates = [int(input()) for _ in range(N)]
sushi_cnt = [0] * (d+1)

# 초기화
cur_cnt = 0
for i in range(k):
    cur = plates[i]
    if sushi_cnt[cur] == 0:
        cur_cnt += 1
    sushi_cnt[cur] += 1

# 쿠폰
result = cur_cnt
if sushi_cnt[c] == 0:
    result += 1


# 탐색
for i in range(1,N):
    pre_sushi = plates[i-1]
    sushi_cnt[pre_sushi] -= 1
    if sushi_cnt[pre_sushi] == 0:
        cur_cnt -= 1

    next_sushi = plates[(i + k -1) % N]
    if sushi_cnt[next_sushi] == 0:
        cur_cnt += 1
    sushi_cnt[next_sushi] += 1

    max_cnt = cur_cnt
    if sushi_cnt[c] == 0:
        max_cnt += 1

    result = max(result, max_cnt)

print(result)