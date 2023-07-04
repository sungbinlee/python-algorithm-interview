"""
Chapter 01 - Problem 02 - 문자열 뒤집기 - https://leetcode.com/problems/reverse-string/

문제 설명:
문자열을 뒤집는 함수를 작성하라. 입력값은 문자 배열이며, 리턴 없이 리스트 내부를 직접 조작하라.

예제 1:
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

예제 2:
Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

풀이 1:
주어진 리스트를 뒤집기 위해서는 리스트의 양쪽 끝에서부터 원소를 교환하는 방식을 
사용합니다. 
- `left` 변수는 리스트의 가장 왼쪽 인덱스를 가리키고, `right` 변수는 리스트의 가장 
오른쪽 인덱스를 가리킵니다.
- `left`가 `right`보다 작은 동안, 즉 리스트의 중간까지 반복하면서 `left`와 
`right` 인덱스의 원소를 교환합니다.
- 교환 후에는 `left` 인덱스를 우측으로 한 칸 이동하고, `right` 인덱스를 좌측으로 한 
칸 이동합니다.
- 이러한 과정을 반복하면 리스트가 뒤집힙니다.

풀이 2:
파이썬에서는 리스트의 뒤집기를 간편하게 수행할 수 있는 내장 함수 `reverse()`를 제공합니다.
- `s.reverse()`를 호출하면 주어진 리스트 `s`가 제자리에서 뒤집히게 됩니다.
- 따라서 풀이 1에서 수행한 교환 과정을 직접 구현할 필요 없이, 내장 함수를 사용하여 뒤집을 수 있습니다.
"""

def reverseString(self, s: List[str]) -> None:
    left, right = 0, len(s) - 1
    while left < right:
        # 현재 left와 right 인덱스의 원소를 교환합니다.
        s[left], s[right] = s[right], s[left]
        left += 1 # left 인덱스를 우측으로 이동합니다.
        right -= 1 # right 인덱스를 좌측으로 이동합니다.

# Pythonic way
def reverseString(self, s: List[str]) -> None:
    s.reverse() # 함수를 사용하여 리스트를 뒤집습니다.