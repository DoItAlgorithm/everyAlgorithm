"""
에라테스 체(?) 이용해서 소수 테이블을 만들어서 해결하려고 했는데, 어느 숫자까지 탐색해서 테이블의 크기를 만들어야 하는지 기준 세우는게 어려웠음

문제 특성 상 수가 랜덤적이고 0에 따라 자르는 수를 넣어 크기가 크지 않을 것이라 예상하여 그때마다 수의 소수 여부를 진단하는 메서드를 사용하기로 함.
"""
def transfer(num, k):
    st = ''
    while num >= 1:
        st += str(num % k) # 나머지 값은 변환한 수를 담는 deque에 넣어준다.
        num //= k  # 몫만 남도록 나눠준다.
    return st[::-1] # 반대로 출력

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) +1):
        if num % i == 0:
            return False
    return True
def count_fit_case(num_str_list):
    count = 0
    tmp_str_num = ''
    for i in range(len(num_str_list)):
        if num_str_list[i] == '0' and len(tmp_str_num) > 0:
            if is_prime(int(tmp_str_num)):
                count += 1
            tmp_str_num = ''
        else:
            tmp_str_num += num_str_list[i]

    # 마지막에 남은 문자열을 count해준다.
    if len(tmp_str_num) > 0:
        if is_prime(int(tmp_str_num)):
            count += 1

    return count
def solution(v,k):
    num_str_list = transfer(v, k)
    answer = count_fit_case(num_str_list)
    return answer
