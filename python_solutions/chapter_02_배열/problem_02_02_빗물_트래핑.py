"""
Chapter 02 - Problem 02 - 빗물 트래핑 - https://leetcode.com/problems/trapping-rain-water/

문제 설명:
높이를 입력받아 비 온 후 얼마나 많은 물이 쌓일 수 있는지 계산하라.

예제:
Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6


풀이1: 높이를 입력받아 비 온 후 얼마나 많은 물이 쌓일 수 있는지 계산하는 문제입니다.

물이 쌓이는 원리는 변곡점을 기준으로 왼쪽과 오른쪽의 최대 높이를 비교하여 작은 쪽의 
높이에서 현재 높이를 뺀 값을 물의 부피로 계산합니다.

높이를 저장하는 리스트와 좌우 포인터를 사용하여 문제를 해결합니다. 좌우 포인터를 배열의 
양쪽 끝에서 시작하고, 좌우 포인터가 서로 만날 때까지 반복합니다.

각 포인터의 위치에서 최댓값을 갱신하면서 물의 부피를 계산합니다. 왼쪽 포인터와 오른쪽 
포인터 중 작은 높이를 선택하여 현재 위치의 높이를 뺀 값을 물의 부피에 더합니다.

매 반복마다 물의 부피를 갱신하고, 좌우 포인터를 이동시킵니다. 최종적으로 계산된 물의 
부피를 반환합니다.

풀이2: 스택을 활용하여 문제를 해결하는 방법입니다.

스택을 사용하여 변곡점을 저장하면서 물의 부피를 계산합니다.

배열의 모든 원소를 순회하면서 현재 높이와 스택의 최상단 높이를 비교합니다. 현재 높이가 
스택의 최상단 높이보다 큰 경우에는 변곡점입니다.

변곡점을 만날 때마다 스택에서 변곡점을 꺼내고, 스택이 비어있지 않은 경우에는 물의 폭과 
높이를 계산하여 물의 부피에 더합니다.

매 반복마다 스택에 현재 인덱스를 추가합니다.

최종적으로 계산된 물의 부피를 반환합니다.
"""

def trap(self, height: List[int]) -> int:
    # 높이 리스트가 비어있는 경우, 0을 반환
    if not height:
        return 0
    
    # 물의 총 부피를 저장할 변수를 초기화합니다.
    volume = 0
    # 좌우 포인터를 사용해서 배열의 양쪽 끝에서 시작합니다.
    left, right = 0, len(height) - 1
    # 좌우 포인터의 높이 값을 저장하는 변수를 초기화 합니다.
    left_max, right_max = height[left], height[right]

    # 좌우 포인터가 서로 만나기 전까지 반복
    while left < right:
        #현재 포인터 위치의 높이와 이전까지의 최댓값을 비교하여 최댓값을 갱신합니다.
        left_max, right_max = max(height[left], left_max), max(height[right], right_max)
        # 왼쪽 높이가 오른쪽 높이보다 작거나 같은 경우,
        if left_max <= right_max:
            # 물 부피를 계산하고, 왼쪽 포인터를 한 칸 우측으로 이동합니다.
            volume += left_max - height[left]
            left += 1
        # 오른쪽 높이가 왼쪽 높이보다 작은 경우,
        else:
            # 물 부피를 계산하고, 오른쪽 포인터를 한 칸 좌측오르 이동합니다.
            volume += right_max - height[right]
            right -= 1
    # 물의 총 부피를 반환합니다.
    return volume


def trap(self, height: List[int]) -> int:
    # 스택을 초기화합니다.
    stack = []
    # 물의 총 부피를 저장할 변수를 초기화합니다.
    volume = 0
    
    # 배열의 모든 원소를 순회하며 물을 채우는 작업을 수행합니다.
    for i in range(len(height)):
        # 현재 높이가 스택의 최상단 높이보다 큰 경우에는
        while stack and height[i] > height[stack[-1]]:
            # 스택에서 꺼냅니다.
            top = stack.pop()

            # 스택이 비어있는 경우, 변곡점이 없으므로 브레이크 합니다.
            if not len(stack):
                break

            # 물의 폭을 계산합니다.
            distance =  i - stack[-1] - 1
            # 물의 높이를 계산합니다. (낮은 높이 - 변곡점 높이)
            waters = min(height[i], height[stack[-1]]) - height[top]

            #물의 총 부피에 현재 구간의 물 부피를 더합니다.
            volume += distance * waters

        # 현재 인덱스를 스택에 추가합니다.
        stack.append(i)
    # 물의 총 부피를 반환합니다.
    return volume