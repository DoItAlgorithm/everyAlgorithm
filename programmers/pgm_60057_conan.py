"""
프로그래머스 60057번
s의 길이가 최대 1000이기 때문에 브루트포스 방식으로도 충분히 구현 가능하다고 생각함.
따라서 1개로 쪼갤때부터 문자열의 반토막까지 쪼개 문자열 길이를 직접 셀 수 있도록 구현함.
"""

def solution(s):
    min_value = len(s)  # 초기값을 문자열 전체 길이로 설정해둠
    for i in range(1, len(s) // 2 + 1):  #1부터 반토막까지 쪼갬
        pre = None
        current = ""
        count = 1
        result = ""

        for j in range(0, len(s), i):
            current = s[j:j + i]
            if pre == current:
                count += 1
            else:
                if pre:  # 이전 문자열이 있다면 결과에 추가
                    if count == 1:
                        result += pre
                    else:
                        result += str(count) + pre
                pre = current
                count = 1

        # 쪼개고 남은 마지막 문자열 추가
        if pre:
            if count == 1:
                result += pre
            else:
                result += str(count) + pre

        if min_value > len(result):
            min_value = len(result)

    return min_value
