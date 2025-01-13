from collections import deque

N, d, k, c = map(int,input().split())
plates = [int(input()) for _ in range(N)]

seq = deque(plates[:k])
answer = len(set(list(seq) + [c]))

for i in range(N):
    seq.popleft()
    seq.append(plates[(i+k) % N])
    answer = max(len(set(list(seq) + [c])), answer)

print(answer)