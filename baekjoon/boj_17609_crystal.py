def is_palindrome(string, left, right):
    while left < right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1
    return True

def solution():
    left = 0
    right = len(in_str) - 1

    while left < right:
        if in_str[left] != in_str[right]:
            if is_palindrome(in_str, left+1, right) or is_palindrome(in_str, left, right-1):
                return 1
            else:
                return 2
        left += 1
        right -= 1

    return 0

T = int(input())
for _ in range(T):
    in_str = input()
    print(solution())
