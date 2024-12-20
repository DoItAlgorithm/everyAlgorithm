from collections import deque

map_N = int(input())
# 좌표 입력은 1,1부터 들어온다.
apple_map = [[False] * (map_N+1) for _ in range(map_N+1)]
snape_map = [[False] * (map_N+1) for _ in range(map_N+1)]
move_info = dict()
dc = [1,0,-1,0] # idx 0 부터 오른쪽 방향에서 1씩 증가하면 오른쪽으로 도는것. 왼쪽으로 도는 것은 -1
dr = [0,1,0,-1]

# 초기화
snape_map[1][1] = True
snape_deque = deque([(1,1)]) # 왼쪽일 수록 꼬리고, 오른쪽일 수록 머리를 뜻한다.
snape_heading = 0

# 사과 위치 채우기
for _ in range(int(input())):
    r,c = map(int,input().split())
    apple_map[r][c] = True
# 방향 변환 정보 담기
for _ in range(int(input())):
    x, heading = input().split()
    move_info[int(x)] = heading

second = 0
while True:
   second += 1

   nr = snape_deque[-1][0] + dr[snape_heading]
   nc = snape_deque[-1][1] + dc[snape_heading]

   if nr <= 0 or nr > map_N or nc <= 0 or nc > map_N or snape_map[nr][nc] :
       break

   # 1. 뱀의 이동을 기록한다.
   snape_map[nr][nc] = True
   snape_deque.append((nr,nc))

   # 2. 사과의 유무에 따라 꼬리를 제거하거나 사과 먹은 처리 해준다.
   if apple_map[nr][nc]:
       apple_map[nr][nc] = False
   else:
       pr,pc = snape_deque.popleft()
       snape_map[pr][pc] = False

   # 3. 회전에 대한 지침이 있는 초면, 다음을 위해 방향을 바꾼다.
   if move_info.get(second):
       command = move_info[second]
       if command == 'D':
           snape_heading = (snape_heading + 1) % 4
       else:
           snape_heading = (snape_heading - 1) % 4


print(second)