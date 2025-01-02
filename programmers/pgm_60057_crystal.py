"""
문자열은 제일 앞부터 정해진 길이만큼 잘라야 한다.
s는 1 ~ 1000이하 , 탐색 시 O(N^2)까지 가능
"""
def solution(s):
    answer = len(s)  # 초기값은 문자열 전체 길이로 설정
    if answer == 1:
        return answer
    for i in range(1,len(s)//2 + 1): #  청크 길이를 1부터 문자열 절반까지 탐색
        compressed = ""  # 압축 결과
        pre = s[:i]
        count = 1

        for j in range(i, len(s), i):
            if pre == s[j:j+i]:
                count += 1
            else:
                if count > 1 :
                    compressed += str(count) + pre
                else:
                    compressed += pre

                pre = s[j:j+i]
                count = 1

        if count > 1:
            compressed += str(count) + pre
        else:
            compressed += pre

        answer = min(answer, len(compressed))
    return answer
