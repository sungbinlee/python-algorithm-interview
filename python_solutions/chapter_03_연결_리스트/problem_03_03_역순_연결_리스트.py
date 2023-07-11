"""
Chapter 03 - Problem 03 - 역순 연결 리스트 - https://leetcode.com/problems/reverse-linked-list/

문제 설명:
연결 리스트를 뒤집어라

예제:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

풀이1: 
재귀적인 방법으로 연결 리스트를 뒤집습니다. 함수 `reverse`를 정의하여 현재 노드와 이전 
노드를 인자로 받아 뒤집힌 연결 리스트를 반환하는 재귀 호출을 수행합니다. 재귀 호출을 통해 
현재 노드의 다음 노드를 임시 변수 `next`에 저장하고, 현재 노드의 다음 노드를 이전 
노드로 설정하여 연결을 뒤집습니다. 이후, 재귀적으로 다음 노드와 현재 노드를 전달하여 
호출합니다. 초기 호출은 head와 이전 노드를 None으로 설정하여 시작합니다.


풀이2:
반복적인 방법으로 연결 리스트를 뒤집습니다. 현재 노드와 이전 노드를 초기화한 후, 현재 
노드를 한 노드씩 이동하면서 연결을 뒤집습니다. 현재 노드의 다음 노드를 임시 변수 
`next`에 저장하고, 현재 노드의 다음 노드를 이전 노드로 설정하여 연결을 뒤집습니다. 
이후, 이전 노드와 현재 노드를 갱신합니다. 마지막에는 이전 노드가 뒤집힌 연결 리스트의 
새로운 head가 됩니다.

"""
# 재귀
def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    def reverse(node: ListNode, prev: ListNode = None):
        # 현재 노드가 None이면 이전 노드를 반환
        if not node:
            return prev
        # 다음 노드를 임시 변수 next에 저장하고, 현재 노드의 다음 노드를 이전 노드로 설정
        next, node.next = node.next, prev
        # 재귀적으로 다음 노드와 현재 노드를 전달하여 호출
        return reverse(next, node)
    # 초기 호출은 head와 이전 노드 None으로 설정
    return reverse(head)

# 반복
def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    # 현재 노드와 이전 노드를 초기화
    node, prev = head, None

    while node:
        # 다음 노드를 임시 변수 next에 저장하고, 현재 노드의 다음 노드를 이전 노드로 설정
        next, node.next = node.next, prev
        # 이전 노드와 현재 노드를 갱신
        prev, node = node, next
    # 마지막에는 이전 노드가 뒤집힌 연겨 릴스트의 새로운 head가 됨
    return prev