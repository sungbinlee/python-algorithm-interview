"""
Chapter 02 - Problem 04 - 배열 파티션 1 - https://leetcode.com/problems/array-partition/

문제 설명:
n개의 페어를 이용한 min(a, b)의 합으로 만들 수 있는 가장 큰 수를 출력하라.

예제:
Input: nums = [1,4,3,2]
Output: 4

풀이1:
주어진 리스트를 정렬하고, 순서대로 2개씩 묶어서 최솟값을 구한 후, 이 최솟값들의 합을 구하는 방식입니다.

풀이2:
주어진 리스트를 정렬하고, 인덱스가 짝수인 경우에만 해당 값을 합에 더하는 방식입니다.

풀이3:
주어진 리스트를 정렬한 후, 슬라이싱을 사용하여 짝수 인덱스의 값들을 선택하고 그 합을 구하는 방식입니다.

모든 풀이 방법은 주어진 리스트를 정렬하여 최솟값을 선택하는 아이디어를 활용하고 있으며, 풀이3은 간결한 코드로 작성되어 있습니다.
"""

# 풀이1: 오름차순 풀이
def arrayPairSum(self, nums: List[int]) -> int:
    sum = 0 # 변수 sum을 0으로 초기화
    pair = [] # 비어있는 리스트 pair 생성
    nums.sort() # nums 리스트를 오름차순으로 정렬

    for n in nums: 
        pair.append(n) # pair 리스트에 현재 요소 n을 추가
        if len(pair) == 2: # pair의 length가 2일 경우
            sum += min(pair) # pair 리스트의 최솟값을 sum에 더함
            pair = [] # pair 리스트 초기화

    return sum # 결과값 반환

# 풀이2: 짝수 번째 값 계산
def arrayPairSum(self, nums: List[int]) -> int:
    sum = 0
    nums.sort()

    for i, n in enumerate(nums):
        if i % 2 == 0: # 인덱스 i가 짝수일 경우
            sum += n # nums[i]를 sum에 더함

# 풀이3: 파이썬다운 방식
def arrayPairSum(self, nums: List[int]) -> int:
    return sum(sorted(nums)[::2])