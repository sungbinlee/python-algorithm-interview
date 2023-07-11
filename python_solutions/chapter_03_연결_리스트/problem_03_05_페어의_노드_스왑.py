"""
Chapter 03 - Problem 05 - 페어의 노드 스왑 - https://leetcode.com/problems/swap-nodes-in-pairs/

문제 설명:
연결 리스트를 입력받아 페어 단위로 스왑하라

예제:
Input: head = [1,2,3,4]
Output: [2,1,4,3]

풀이1: 값만 교환
현재 노드와 다음 노드의 값을 교환하여 노드 쌍을 스왑하는 방식입니다.

풀이2: 반복 구조로 스왑
더미 노드인 root와 이전 노드인 prev를 사용하여 연결 리스트의 노드 쌍을 스왑하는 방식입니다.
현재 노드와 다음 노드가 모두 존재하는 동안 반복하여 스왑합니다.

풀이3: 재귀 구조로 스왑
재귀적인 방식으로 연결 리스트의 노드 쌍을 스왑합니다.
현재 노드와 다음 노드가 모두 존재하는 경우에만 스왑하고, 재귀적으로 나머지 노드들을 처리합니다.


"""
# 값만 교환
def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
    cur = head

    # 현재 노드와 다음 노드가 모두 존재하는 동안 반복
    while cur and cur.next:
        # 현재 노드와 다음 노드의 값을 교환
        cur.val, cur.next.val = cur.next.val, cur.val
        # 현재 노드를 다음 노드의 다음 노드로 이동
        cur = cur.next.next

    return head
    
# 반복 구조로 스왑
def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
    root = prev = ListNode(None)
    prev.next = head
    # 현재 노드와 다음 노드가 모두 존재하는 동안 반복
    while head and head.next:
        # 다음 노드
        b = head.next
        # 현재 노드의 다음 노드를 다다음 노드로 설정
        head.next = b.next
        # 다음 노드의 다음 노드를 현재 노드로 설정
        b.next = head
        # 이전 노드의 다음 노드를 다음 노드로 설정
        prev.next = b

        # 현재 노드를 다음 노드로 이동
        head = head.next
        # 이전 노드를 다다음 노드로 이동
        prev = prev.next.next
    return root.next

def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
     # 현재 노드와 다음 노드가 모두 존재하는 경우
    if head and head.next:
        p = head.next # 다음 노드
        # 현재 노드의 다음 노드를 재귀적으로 처리한 결과로 설정
        head.next = self.swapPairs(p.next)
        p.next = head # 다음 노드의 다음 노드를 현재 노드로 설정
        return p # 다음 노드를 시작 노드로 반환
    return head # 노드가 하나 또는 없는 경우, 그대로 반환
