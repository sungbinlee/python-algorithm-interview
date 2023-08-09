"""
Chapter 04 - Problem 01 - 유효한 괄호 - https://leetcode.com/problems/valid-parentheses/

문제 설명:
괄호로 된 입력값이 올바른지 판별하라.

예제:
Input: s = "()[]{}"
Output: true

풀이: 
(, [, {는 스택에 푸쉬하고 },],),를 만날 때 스택에서 팝 한 결과가 매핑 테이블 매칭되는지 확인하고 일치 하지 않으면 False를 반환한다.


"""

def isValid(self, s: str) -> bool:
    stack = [] # 괄호를 저장할 스택 선언
    table = { # 짝을 이루는 괄호들을 저장한 딕셔너리
        ')': '(',
        '}': '{',
        ']': '[',
    }

    for char in s: # 문자열을 순회하면서
        if char not in table: # 열림 괄호일 경우
            stack.append(char) # 스택에 추가
        # 스택이 비어있거나 대응하는 열림 괄호와 일치하지 않는 경우 False 반환
        elif not stack or table[char] != stack.pop(): 
            return False
    return len(stack) == 0 # 스택이 비어있는 경우 True, 그렇지 않은 경우 False 반환