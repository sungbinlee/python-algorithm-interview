"""
Chapter 01 - Problem 01 - 유효한 팰린드롬 - https://leetcode.com/problems/valid-palindrome/

문제 설명:
주어진 문자열이 팰린드롬인지 확인하라. 대소문자를 구분하지 않으며, 영문자와 숫자만을 대상으로 한다.

예제 1:
"A man, a plan, a canal: Panama" -> true

예제 2:
"race a car" -> false

풀이 1은 주어진 문자열을 리스트로 변환하여 팰린드롬 여부를 확인하는 방법입니다. 주어진 
문자열을 순회하면서 영문자와 숫자만 추출하여 리스트에 저장하고, 리스트의 맨 앞과 맨 뒤의 
값을 비교하여 팰린드롬 여부를 판별합니다.

풀이 2는 데크(deque) 자료형을 사용하여 풀이 1의 시간 복잡도를 최적화한 방법입니다. 
데크는 양쪽에서 원소의 삽입과 삭제가 가능한 자료구조로, 리스트와 유사한 동작을 수행할 수 
있습니다. 따라서 리스트의 맨 앞에서 pop(0)을 하는 연산은 선형 시간 복잡도를 가지는 
반면, 데크에서는 O(1)의 시간 복잡도를 가지므로 효율적으로 팰린드롬 여부를 확인할 수 있습니다.

풀이 3:
풀이 3은 슬라이싱을 사용하여 주어진 문자열을 처리하여 팰린드롬 여부를 확인하는 
방법입니다. 우선 문자열을 소문자로 변환하고, 정규표현식을 사용하여 영문자와 숫자 이외의 
문자를 필터링합니다. 그 후, 슬라이싱을 통해 문자열을 뒤집은 것과 원래 문자열을 비교하여 
팰린드롬 여부를 판별합니다. 슬라이싱 연산은 C 언어 수준에서 구현되어 있어서 매우 
효율적입니다. 문자열의 뒤집기와 비교 과정이 내부적으로 최적화되어 실행 시간을 줄일 수 있습니다.
"""

# 리스트로 변환
def isPalindromeList(self, s: str) -> bool:
    strs = [] # 문자를 저장할 빈 리스트를 생성
    # 입력 문자열의 각 문자를 순회합니다.
    for char in s: 
        if char.isalnum(): # 문자가 영문/숫자 인지 확인합니다.
            strs.append(char.lower()) # 소문자로 변환한 문자를 리스트에 추가합니다.
    
    #팰린드롬 여부를 확인합니다.
    while len(strs) > 1: # 문자가 1개 이상 남아있는 동안 반복합니다.
        if strs.pop(0) != strs.pop(): # 맨 앞의 값과 맨 뒷부분의 값을 비교합니다.
            return False # 비교 결과가 다르다면 False를 반환합니다.
        
    return True # 모든 문자가 일치하면 True를 반환합니다.

# 데크 자료형을 이용한 최적화
import collections; # 데크 자료형을 사용하기 위해 collection 모듈을 임포트 합니다.
def isPalindromeDeque(self, s: str) -> bool:
    strs: Deque = collections.deque()
    # 입력 문자열의 각 문자를 순회합니다.
    for char in s: 
        if char.isalnum(): # 문자가 영문/숫자 인지 확인합니다.
            strs.append(char.lower()) # 소문자로 변환한 문자를 리스트에 추가합니다.
    
    #팰린드롬 여부를 확인합니다.
    while len(strs) > 1: # 문자가 1개 이상 남아있는 동안 반복합니다.
        if strs.pop(0) != strs.pop(): # 맨 앞의 값과 맨 뒷부분의 값을 비교합니다.
            return False # 비교 결과가 다르다면 False를 반환합니다.
        
    return True # 모든 문자가 일치하면 True를 반환합니다.

# 슬라이싱 사용
import re  # 정규표현식을 사용하기 위해 re 모듈을 임포트합니다.
def isPalindrome(self, s: str) -> bool:
    s = s.lower() # 문자열을 소문자로 변환합니다.
    s = re.sub('[^a-z0-9]', '', s) # 정규표현식을 사용하여 영문/숫자 이외의 문자를 필터링합니다.

    return s == s[::-1] # 문자열을 뒤집은 것과 원래 문자열을 비교하여 결과를 반환합니다.