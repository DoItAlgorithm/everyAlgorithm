"""
재방문을 할 수 있다는 점에서 bfs를 떠올리기 힘들었음.

이 문제를 통해 재방문 가능한 bfs 기법을 배움
"""
from collections import deque

def find_shortest(start, goal):
    distance = [0] * 100_001  # idx : 위치 , 각 위치에 도착하기 까지 필요한 step을 값으로 가짐
    case_cnt = 0
    shortest_dist = 0
    dQ = deque([start])

    while dQ:
        cur_point = dQ.popleft()

        if cur_point == goal:
            shortest_dist = distance[cur_point]
            case_cnt += 1
            continue

        # 움직일 수 있는 방향으로 후보를 dQ에 넣어준다.
        for next_point in [cur_point + 1, cur_point - 1, cur_point * 2]:
            # 탐색 후보가 되는 조건들 추가
            if 0 <= next_point < 100_001:
                 # 다음 위치에 한 번도 안 가봤거나, 지금 위치까지 오는 step +1 과 다음 위치의 step과 같으면 최소값 유지 가능
                if distance[next_point] == 0 or distance[cur_point] + 1 == distance[next_point]:
                    distance[next_point] = distance[cur_point] + 1
                    dQ.append(next_point)

    return shortest_dist, case_cnt


start_point, goal_point = map(int, input().split())
result1, result2 = find_shortest(start_point, goal_point)
print(result1)
print(result2)
