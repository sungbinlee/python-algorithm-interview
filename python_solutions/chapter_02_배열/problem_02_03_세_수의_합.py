"""
Chapter 02 - Problem 03 - 세 수의 합 - https://leetcode.com/problems/3sum/

문제 설명:
배열을 입력받아 합으로 0을 만들 수 있는 3개의 엘리먼트를 출력하라.

예제:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

풀이1:
이 문제는 브루트 포스 방식으로 해결할 수 있습니다. 세 수를 모두 확인하여 합이 0이 되는 경우를 찾습니다. 먼저 주어진 배열을 오름차순으로 정렬한 뒤, 첫 번째 숫자를 기준으로 잡고 두 번째, 세 번째 숫자를 차례대로 확인하여 합이 0이 되는 조합을 찾습니다. 중복된 값을 건너뛰기 위해 조건문을 추가로 사용합니다. * 시간 복잡도가 O(n^3)으로 매우 크기 때문에, 입력이 클 경우에는 성능이 좋지 않을 수 있습니다.

풀이2:
이 문제는 투포인터 방식으로도 해결할 수 있습니다. 주어진 배열을 오름차순으로 정렬한 뒤, 첫 번째 숫자를 기준으로 두 번째와 세 번째 숫자의 합을 조정하며 0을 찾습니다. 합이 0보다 작으면 두 번째 숫자를 증가시켜 합을 키우고, 합이 0보다 크면 세 번째 숫자를 감소시켜 합을 줄입니다. 만약 합이 0이 되면 결과 리스트에 추가하고, 중복된 값을 건너뛰기 위해 조건문과 while 루프를 사용합니다. * 투포인터 방식으로 문제를 해결하므로, 시간 복잡도를 O(n^2)로 개선할 수 있습니다.
"""

# 브루트 포스 n^3 풀이
def threeSum(self, nums: List[int]) -> List[List[int]]:
    results = [] # 결과를 담을 리스트 초기화
    nums.sort() # 입력 리스트를 오름차순으로 정렬

    for i in range(len(nums) - 2):
        # 중복된 값 건너뛰기
        if i > 0 and nums[i] == nums[i-1]:
            continue
        for j in range(i + 1, len(nums) - 1):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            for k in range(j + 1, len(nums)):
                if k > j + 1 and nums[k] == nums[k - 1]:
                    continue
                if nums[i] + nums[j] + nums[k] == 0: # 합이 0인 경우
                    results.append([nums[i], nums[j], nums[k]]) # 결과 리스트에 추가

    return results # 결과 리스트 반환

# 투포인터로 합 계산
def threeSum(self, nums: List[int]) -> List[List[int]]:
    results = []  # 결과를 담을 리스트 초기화
    nums.sort()  # 입력 리스트를 오름차순으로 정렬

    for i in range(len(nums) - 2):
    # 중복된 값 건너뛰기
        if i > 0 and nums[i] == nums[i-1]:
            continue
            
        # 간격을 좁혀가면서 계산하는 투포인터 방식
        left, right = i + 1, len(nums) - 1 # 두 번째와 세 번째 숫자의 포인터 설정
        while left < right: # 왼쪽 포인터가 오른쪽보다 작을 때까지
            sum = nums[i] + nums[left] + nums[right] # 세 숫자의 합 계산
            if sum < 0: # 합이 0보다 작은경우, 두번째 숫자를 큰쪽으로 이동
                left += 1
            elif sum >0: # 합이 0보다 큰경우, 세번째 숫자를 작은쪽으로 이동
                right -= 1
            else: # 합의 0인 경우
                results.append([nums[i], nums[left], nums[right]])
                # 결과 리스트에 추가
                # 중복된 값 건더 뛰기
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1 # 다음 두 번째 숫자로 이동
                right -= 1 # 다음 세 번째 숫자로 이동
        return results # 결과 리스트 반환