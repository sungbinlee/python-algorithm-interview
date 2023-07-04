"""
Chapter 02 - Problem 06 - 주식을 사고팔기 가장 좋은 시점 - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

문제 설명:
한 번의 거래로 낼 수 있는 최대 이익을 산출하라.

예제:
Input: prices = [7,1,5,3,6,4]
Output: 5

풀이1: 
브루트 포스 방식으로 모든 가능한 주식 가격 조합을 비교하여 최대 이익을 계산하는 
풀이입니다. 이중 반복문을 사용하여 모든 가능한 주식 가격 조합에 대해 현재 가격과 이후 
가격들을 비교하여 최대 이익을 갱신합니다. 이때, max 함수를 사용하여 현재까지의 최대 
이익과 비교하고 갱신합니다.

풀이2:
효율적인 방법으로 주어진 주식 가격 리스트에서 최대 이익을 계산합니다.
단일 반복문을 사용하여 주식 가격을 순회하면서 최소 가격을 갱신하고, 이전 최소 가격과 현재 
가격 차이를 계산하여 최대 이익을 갱신합니다. 이때, min 함수와 max 함수를 사용하여 각각 
최소 가격과 최대 이익을 갱신합니다.
"""

# 브루트 포스로 계산
def maxProfit(self, prices: List[int]) -> int:
    max_price = 0

    for i, price in enumerate(prices): # 주식 가격을 순회하면서
        for j in range(i, len(prices)): # 현재 가격부터 마지막 가격까지 비교
            max_price = max(prices[j] - price, max_price) # 최대 이익을 갱신
    
    return max_price

# 효율적인 방법
def maxProfit(self, prices: List[int]) -> int:
    max_profit = 0
    min_price = float('inf')  # 최소 가격을 초기화

    for price in prices: # 주식 가격을 순회 하면서
        min_price = min(min_price, price)  # 최솟값 갱신
        max_profit = max(max_profit, price - min_price)  # 최대 이익 갱신
    
    return max_profit