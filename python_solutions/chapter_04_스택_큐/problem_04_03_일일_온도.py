"""
Chapter 04 - Problem 03 - 일일 온도 - https://leetcode.com/problems/daily-temperatures/

문제 설명:
매일의 화씨 온도 리스트 T를 입력받아서, 더 따뜻한 날씨를 위해서는 며칠을 더 기다려야 하는지를 출력하라

예제:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

풀이:
주어진 온도 리스트를 순회하면서 스택을 활용하여 현재 온도보다 더 높은 온도를 가진 날짜들을 추적합니다. 스택에는 현재까지 가장 따뜻한 날짜의 인덱스를 유지합니다. 만약 현재 온도가 스택의 가장 위의 온도보다 높다면, 스택에서 가장 위의 온도를 꺼내고 해당 온도의 인덱스에 대응하는 결과 리스트 값을 갱신합니다. 이 과정을 모든 날짜에 대해 반복하여 결과 리스트를 완성한 후 반환합니다.

"""

def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    # 결과 리스트를 0으로 초기화
    answer = [0] * len(temperatures)
    stack = []
    # 온도 리스트를 순회하면서 인덱스와 현재 온도를 가져옴
    for i, cur in enumerate(temperatures):
        # 스택이 비어있지 않고, 현재 온도가 스택의 가장위의 온도보다 높은 경우
        while stack and cur > temperatures[stack[-1]]:
            # 스택에서 가장 위의 온도의 인덱스를 가져옴
            last = stack.pop()
            # 해당 온도의 인덱스에 대응하는 결과 리스트의 값을 갱신
            answer[last] = i - last
        #현재 온도의 인덱스를 추가
        stack.append(i)

    return answer