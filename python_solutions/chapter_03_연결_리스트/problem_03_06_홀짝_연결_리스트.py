"""
Chapter 03 - Problem 06 - 홀짝 연결 리스트 - https://leetcode.com/problems/odd-even-linked-list/

문제 설명: 
연결 리스트를 홀수 노드 다음에 짝수 노드가 오도록 재구성하라. 공간 복잡도O(1) 시간복잡도 O(n)에 풀이하라.

예제:
Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]

풀이:
홀수 노드와 짝수 노드를 순차적으로 연결하여 연결 리스트를 재구성합니다. 
"""

def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    # 헤드가 None인 경우 예외처리
    if head is None:
        return None
    
    odd = head # 홀수 노드의 시작노드
    even = head.next # 짝수 노드의 시작노드
    even_head = head.next # 짝수 노드의 헤드 노드

    while even and even.next: # 홀수 노드 짝수 노드가 모두 존재하는 동안 반복
        odd.next, even.next = odd.next.next, even.next.next # 홀수 노드와 짝수 노드를 연결
        odd, even = odd.next, even.next # 홀수 노드와 짝수 노드를 갱신

    odd.next = even_head # 홀수 노드의 마지막을 짝수 노드의 헤드로 연결
    return head # 변경된 연결 리스트의 헤드 반환