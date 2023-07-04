"""
Chapter 02 - Problem 01 - 두 수의 합 - https://leetcode.com/problems/two-sum/

문제 설명:
덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라.

예제:
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]


풀이1: 브루트포스
첫 번째 풀이는 모든 가능한 조합을 확인하여 두 수의 합이 목표값과 일치하는지 확인하는 
브루트포스 방법입니다. 이중 반복문을 사용하여 모든 숫자 쌍을 비교합니다. 두 수의 합이 
목표값과 일치하면 해당 인덱스를 반환합니다.

장점: 간단하고 직관적인 방법으로 구현할 수 있습니다.
단점: 모든 가능한 조합을 확인하기 때문에 시간 복잡도가 O(n^2)입니다. 큰 입력에 대해서는 
비효율적일 수 있습니다.

풀이2: in을 이용한 탐색
두 번째 풀이는 현재 수의 보수를 계산하여 보수가 배열의 나머지 부분에 있는지 확인하는 
방법입니다. 이를 위해 enumerate 함수를 사용하여 현재 수와 인덱스를 동시에 확인합니다. 
보수가 배열의 나머지 부분에 있다면 현재 수와 보수의 인덱스를 반환합니다.

장점: 한 번의 반복문으로 문제를 해결할 수 있습니다. 시간 복잡도가 O(n)입니다.
단점: in 연산을 사용하여 배열에서 보수를 찾기 때문에 루프 내에서 선형 탐색이 필요합니다. 
보수를 찾는 과정에서 추가적인 시간이 소요될 수 있습니다.

풀이3: 시간복잡도 개선
세 번째 풀이는 딕셔너리를 활용하여 한 번의 순회로 문제를 해결합니다. 먼저 수와 해당 수의 
인덱스를 매핑하기 위한 딕셔너리를 생성합니다. 배열을 순회하며 수와 인덱스를 딕셔너리에 
저장합니다. 그 후, 배열을 다시 순회하며 보수의 존재 여부를 딕셔너리에서 확인합니다. 
보수가 존재하고 현재 인덱스와 보수의 인덱스가 서로 다른 경우 해당 인덱스를 반환합니다.

장점: 한 번의 반복문으로 문제를 해결하며, 딕셔너리를 활용하여 빠른 보수 검색이 
가능합니다. 시간 복잡도가 O(n)입니다.
단점: 딕셔너리를 사용하여 공간 복잡도가 O(n)이 됩니다. 추가적인 공간을 사용해야 하므로 
메모리를 더 소비합니다.
"""

def twoSum(self, nums: List[int], target: int) -> List[int]:
    # 배열을 순회하며 모든 가능한 조합을 확인합니다.
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            # 두 수의 합이 목표값과 일치하는지 확인합니다.
            if nums[i] + nums[j] == target:
                # 인덱스를 반환합니다.
                return [i, j]

def twoSum(self, nums: List[int], target: int) -> List[int]:
    # 배열을 순회하며 현재 수의 보수를 계산합니다.
    for i, n in enumerate(nums):
        complement = target - n
        # 보수가 배열의 나머지 부분에 있는지 확인합니다.
        if complement in nums[i + 1]:
            # 현재 수와 보수의 인덱스를 반환합니다.
            return [nums.index(n), nums[i + 1:].index(complement) + (i + 1)]

def twoSum(self, nums: List[int], target: int) -> List[int]:
    # 수와 해당 수의 인덱스를 매핑하기 위한 딕셔너리를 생성합니다.
    nums_map = {}
    # 배열을 순회하며 수와 인덱스를 딕셔너리에 저장합니다.
    for i, num in enumerate(nums):
        nums_map[num] = i
    # 배열을 다시 순회하며 보수의 존재 여부를 확인합니다.
    for i, num in enumerate(nums):
        if target - num in nums_map and i != nums_map[target-num]:
            # 현재 수와 보수의 인덱스를 반환합니다.
            return [i, nums_map[target - num]]