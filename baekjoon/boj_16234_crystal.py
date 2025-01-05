from collections import deque
N, L, R = map(int,input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]
def find_chunk(start_r, start_c):
    dQ = deque([(start_r, start_c)])
    visited[start_r][start_c] = True
    chunk = [(start_r, start_c)]

    while dQ:
        r, c = dQ.popleft()
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                if L <= abs(maps[r][c] - maps[nr][nc]) <= R:
                    dQ.append((nr,nc))
                    chunk.append((nr,nc))
                    visited[nr][nc] = True

    if len(chunk) <= 1:
        return 0
    share_result = sum(maps[r][c] for r,c in chunk) // len(chunk)
    for r,c in chunk:
        maps[r][c] = share_result
    return 1

count = 0
while True:
    visited = [[False] * N for _ in range(N)]
    can_make_chunk = 0
    for r in range(N):
        for c in range(N):
            if not visited[r][c]:
                visited[r][c] = True
                can_make_chunk += find_chunk(r,c)
    if can_make_chunk == 0:
        break
    count += 1

print(count)