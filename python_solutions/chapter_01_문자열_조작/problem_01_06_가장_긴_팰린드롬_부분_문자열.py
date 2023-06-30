"""
Chapter 01 - Problem 06 - 가장 긴 팰린드롬 부분 문자열 - https://leetcode.com/problems/longest-palindromic-substring/

문제 설명:
가장 긴 팰린드롬 부분 문자열을 출력하라.

예제:
Input: s = "babad"
Output: "bab"

풀이: 
"""

def longestPalindrome(self, s: str) -> str:
    # 팰린드롬 판별 및 투 포인터 확장 함수
    def expand(left: int, right: int) -> str:
        # 양쪽 포인터가 문자열 범위 내에 있고, 좌우 문자가 동일한 경우 확장한다.
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # 확장한 팰린드롬 부분 문자열 반환
        return s[left + 1:right]
    
    # 문자열 길이가 2 이하이거나 주어진 문자열 자체가 팰린드롬인 경우 빠르게 리턴
    if len(s) < 2 or s == s[::-1]:
        return s
    
    result = ''
    # 슬라이딩 윈도우 우측으로 이동하여 가장 긴 팰린드롬 부분 문자열 찾기
    for i in range(len(s) - 1):
        result = max(result, 
                    expand(i, i + 1), # 홀수 길이의 팰린드롬 확장
                    expand(i, i + 2), # 짝수 길이의 팰린드롬 확장
                    key=len)
    return result