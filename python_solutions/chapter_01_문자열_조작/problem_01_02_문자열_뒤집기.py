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

"""

def reverseString(self, s: List[str]) -> None:
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right += 1