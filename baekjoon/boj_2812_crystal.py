'''
stack 활용 ver
'''

def solution_better():
    remove_cnt = K
    stack = [nums[0]]

    cur = 1
    while cur < N:
        while remove_cnt > 0 and stack and stack[-1] < nums[cur] :
            stack.pop()
            remove_cnt -= 1
        stack.append(nums[cur])
        cur += 1

    return stack[:N-K]


'''
처음엔 deque를 활용해서 풀었다. 
앞 뒤로 다 자유롭게 뺄 수 있어 덱을 애용했었는데, 이런 문제에는 한 쪽으로만 흐름하는 stack이 더 유용했다.
'''
def solution():
    from collections import deque

    num_string = ''.join(map(str, nums))

    result = deque([ num_string[0] ])
    cur = 1
    remove_count = K  # 남은 제거 횟수

    while cur < N:
        while remove_count and result and int(result[-1]) < int(num_string[cur]) :
            result.pop()
            remove_count -= 1

        result.append(num_string[cur])
        cur += 1

    while len(result) > N-K :
        result.pop()

    return result

"""
입출력 부분 
"""
N, K = map(int,input().split())
nums = list(map(int,input()))
result = solution_better()
for num in result:
    print(num, end ='')
