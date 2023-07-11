"""
Chapter 03 - Problem 07 - 역순 연결 리스트 II - https://leetcode.com/problems/reverse-linked-list-ii/

문제 설명: 
인덱스left에서 right 까지 역순으로 만들어라. 인덱스 m은 1부터 시작한다.

예제:
Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]

풀이:
left - 1번째 노드까지 이동하고, 역순으로 만들 부분의 시작 노드인 start와 마지막 노드인 end를 찾습니다. 그 후, 역순으로 만들 부분의 노드들을 뒤집어 연결하고, 변경된 연결 리스트의 헤드 노드를 반환합니다.
"""

def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    # Head가 None이거나 left와 right가 같은 경우 예외 처리
    if not head or left == right: 
        return head
    
    # 가상의 노드 와 start 노드를 초기화
    root = start = ListNode(None)
    root.next = head # root의 다음 노드를 head로 설정

    for _ in range(left - 1): # 역순으로 만들 부분의 시작 노드 찾기
        start = start.next
    end = start.next # 역순으로 만들 부분의 마지막 노드

    for _ in range(right - left): # 역순으로 만들 부분 노드들을 뒤집기
        tmp, start.next, end.next = start.next, end.next, end.next.next
        start.next.next = tmp
    return root.next # 변경된 연결 리스트의 헤드 노드 반환
