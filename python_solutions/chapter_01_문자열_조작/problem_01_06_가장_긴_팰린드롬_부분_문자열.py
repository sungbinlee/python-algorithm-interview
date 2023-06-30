"""
Chapter 01 - Problem 06 - 가장 긴 팰린드롬 부분 문자열 - https://leetcode.com/problems/longest-palindromic-substring/

문제 설명:
가장 긴 팰린드롬 부분 문자열을 출력하라.

예제:
Input: s = "babad"
Output: "bab"

풀이: 
이 문제를 해결하기 위해선 팰린드롬을 판별하는 함수와 투 포인터 확장을 이용합니다.

1. 팰린드롬 판별 함수 expand(left: int, right: int) -> str:
이 함수는 양쪽 포인터가 주어진 문자열 범위 내에 있고, 좌우 문자가 동일한 경우에만 확장하는 역할을 합니다.
while 루프를 통해 양쪽 포인터를 이동시키며, 좌우 문자가 동일할 때까지 확장합니다.
그 후, 확장된 팰린드롬 부분 문자열을 반환합니다.

2. 문자열 길이가 2 이하이거나 주어진 문자열 자체가 팰린드롬인 경우:
이 경우에는 주어진 문자열이 이미 팰린드롬이므로 그대로 리턴합니다.

3. 슬라이딩 윈도우를 이용한 팰린드롬 부분 문자열 탐색:
for 루프를 통해 문자열을 순회하며, 현재 문자를 중심으로 하는 홀수 길이의 팰린드롬과
현재 문자와 다음 문자를 중심으로 하는 짝수 길이의 팰린드롬을 확장합니다.
가장 긴 팰린드롬 부분 문자열을 result 변수에 저장합니다.

4. 최종 결과 반환:
가장 긴 팰린드롬 부분 문자열이 result에 저장되어 있으므로, 이를 반환합니다.
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