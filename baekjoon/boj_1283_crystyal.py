def solution(words, used_alphabet):

    # 1. 각 단어의 첫 문자 확인
    for i,word in enumerate(words):
        if not used_alphabet[word[0].upper()]:
            used_alphabet[word[0].upper()] = 1
            words[i] = '[' + word[0] + ']' + word[1:]
            return words
    # 2. 만약 각 단어 첫 문자에서 키워드가 안 나오면 처음부터 끝까지 확인
    for i,word in enumerate(words):
        for j in range(1,len(word)):
            if not used_alphabet[word[j].upper()]:
                used_alphabet[word[j].upper()] = 1
                words[i] = word[0:j] + '[' + word[j] + ']' + word[j+1:]
                return words
    # 3. 끝내 없으면 원래 문자 반환
    return words

def make_alphabet_dict():
    used_alphabet = dict()
    for al in range(ord('A'), ord('Z') +1):
        used_alphabet[chr(al)] = 0
    return used_alphabet

T = int(input())
used_alphabet = make_alphabet_dict();

for _ in range(T):
    words = input().split()
    answer_list = solution(words, used_alphabet)

    for chars in answer_list:
        print(chars, end=' ')
    print()