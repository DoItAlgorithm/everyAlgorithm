N, MAX_WEIGHT = map(int,input().split())
product_info = []
for _ in range(N):
    product_info.append(list(map(int,input().split()))) # 무게, 가치

dp = [0] * (MAX_WEIGHT+1)

# 시간 복잡도 : 이중 for문 100_000 * 100 = 10_000_000
for w, v in product_info:
    for cur_w in range(MAX_WEIGHT, w - 1, -1):  # 역방향으로 순회
        dp[cur_w] = max(dp[cur_w], dp[cur_w - w] + v)

print(dp[MAX_WEIGHT])
