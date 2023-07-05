"""
Chapter 03 - Problem 02 - 두 정렬 리스트의 병합 - https://leetcode.com/problems/merge-two-sorted-lists/

문제 설명:
정렬되어 있는 두 연결 리스트를 합쳐라.

예제:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

풀이1: 
재귀적으로 두 리스트를 병합합니다. 먼저, 현재 l1과 l2를 비교하여 l1이 더 크다면 두 노드를 교환합니다. 그 다음, l1이 비어있지 않은 경우에는 l1.next부터 시작하는 남은 리스트와 l2를 재귀적으로 병합하고, 그 결과를 l1.next에 할당합니다. 마지막으로, 최종적으로 병합된 리스트인 l1을 반환합니다.

이 풀이는 정렬된 두 연결 리스트를 비교하면서 병합하기 때문에 시간 복잡도는 O(N + M)입니다.
"""
def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    # 만약 l1이 비어있거나, l2가 존재하고 l1의 값이 l2값 보다 크면,
    # l1과 l2를 교환하여 항상 l1이 더 작은 노드를 가르키도록 한다.
    if (not l1) or (l2 and l1.val > l2.val):
        l1, l2 = l2, l1
    if l1:
        # 만약 l1 이 비어있지 않다면,
        # l1.next부터 시작하는 남은 리스트와 l2를 재귀적으로 병합
        # 그 결과를 l1.next에 할당
        l1.next = self.mergeTwoLists(l1.next, l2)
    return l1