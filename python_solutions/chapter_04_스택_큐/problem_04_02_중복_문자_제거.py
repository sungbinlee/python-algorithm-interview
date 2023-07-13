"""
Chapter 04 - Problem 02 - 중복 문자 제거 - https://leetcode.com/problems/remove-duplicate-letters/

문제 설명:
중복된 문자를 제외하고 사전식 순서(Lexicographical Order)로 나열하라.

예제:
Input: s = "bcabc"
Output: "abc"

풀이:
문자열을 순회하면서 스택을 사용하여 중복된 문자들을 제거하고, 최종적으로 스택에 저장된 문자들을 합쳐서 반환합니다. 중복된 문자들을 제거하기 위해 카운터와 집합을 사용하며, 스택을 활용하여 중복된 문자들을 관리합니다.

"""

def removeDuplicateLetters(self, s: str) -> str:
    # 문자열의 빈도수를 저장하는 카운터, 등장한 문자를 저장하는 집합, 스택을 선언
    counter, seen, stack = collections.Counter(s), set(), []

    for char in s: # 문자열을 순회하면서
        counter[char] -= 1 # 현재 문자의 카운터 값을 감소
        if char in seen: # 이미 등장한 문자인 경우 무시
            continue

        # 스택이 비어있지 않고, 현재 문자가 스택의 마지막 문자보다 작고, 스택의 마지막 문자의 빈도수가 0보다 큰동안에는
        while stack and char < stack[-1] and counter[stack[-1]] > 0:
            seen.remove(stack.pop()) # 스택의 마지막 문자를 제거하고, 집합에서도 제거

        stack.append(char)  # 현재 문자를 스택에 추가
        seen.add(char)  # 현재 문자를 집합에 추가

    return ''.join(stack)  # 스택에 저장된 문자들을 합쳐서 반환