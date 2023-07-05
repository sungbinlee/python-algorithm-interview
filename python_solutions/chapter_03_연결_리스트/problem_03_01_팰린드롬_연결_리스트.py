"""
Chapter 03 - Problem 01 - 팰린드롬 연결 리스트 - https://leetcode.com/problems/palindrome-linked-list/

문제 설명:
연결 리스트가 팰린드롬 구조인지 판별하라

예제:
Input: head = [1,2,2,1]
Output: true

풀이1: 
리스트 변환 방식을 사용하여 연결 리스트를 리스트로 변환한 뒤, 양쪽 끝에서부터 요소를 
비교하여 팰린드롬 여부를 확인합니다. 이 풀이의 시간 복잡도는 O(n)입니다. 연결 리스트의 
길이를 n이라고 할 때, 한 번의 순회로 리스트 변환을 수행하고, 양쪽 끝에서부터 요소를 
비교하는 과정은 최대 n/2번 수행되므로 전체적으로 O(n)의 시간 복잡도를 가집니다.

풀이2:
데크(deque)를 사용하여 연결 리스트를 저장하고 양쪽 끝에서부터 요소를 비교하여 팰린드롬 
여부를 확인합니다. 이 풀이는 리스트 변환 방식보다 빠른 실행 시간을 가지며, 데크의 양쪽 
끝에서의 pop 연산이 O(1)의 시간 복잡도를 가지므로 더 효율적입니다.

풀이3:
느린 포인터(slow)와 빠른 포인터(fast) 두 개의 포인터를 사용하였습니다. 느린 포인터는 한 칸씩, 빠른 포인터는 두 칸씩 이동하면서 연결 리스트를 탐색합니다.

이 알고리즘은 다음과 같은 원리로 동작합니다:

1. 빠른 포인터(fast)와 느린 포인터(slow)를 초기에 연결 리스트의 헤드(head)로 설정합니다.
2. 빠른 포인터는 한 번에 두 칸씩 이동하고, 느린 포인터는 한 번에 한 칸씩 이동합니다.
3. 이동하면서 빠른 포인터가 끝에 도달할 때까지 계속 진행합니다.
4. 이동하면서 느린 포인터가 연결 리스트의 중간 지점까지 이동한 후, 중간 이후의 노드들을 
역순으로 연결합니다. 이를 위해 역순으로 연결되는 노드를 가리키는 변수(rev)를 사용합니다.
5. 중간 이후의 노드들을 역순으로 연결한 후, 역순으로 연결된 리스트(rev)와 원래 리스트
(slow)를 비교하며 팰린드롬 여부를 확인합니다.
6. 비교 과정에서 값이 다른 노드가 나오면 팰린드롬이 아니므로 False를 반환합니다.
7. 모든 노드의 값이 일치하면 팰린드롬이므로 True를 반환합니다.

이렇게 빠른/느린 런너 방식을 사용하면 연결 리스트의 중간 위치를 찾거나, 연결 리스트의 반대 방향으로 탐색할 수 있어 다양한 문제에서 활용될 수 있습니다.
"""
# 리스트 변환
def isPalindrome(self, head: Optional[ListNode]) -> bool:
    q: List = [] # 리스트 q 선언 및 초기화

    if not head: 
        return True
    
    node = head # node에 head할당
    while node is not None: # node 가 None이 아닐때 까지
        q.append(node.val) # q 리스트에 현재 노드 값 추가
        node = node.next # 다음 노드로 이동

    while len(q) > 1: # q의 길이가 1보다 클 때까지 
        if q.pop(0) != q.pop(): # q의 첫번째 요소와 마지막 요소를 비교해서 다르면 False
            return False
        
    return True

# 데크를 이용한 풀이(최적화)
def isPalindrome(self, head: Optional[ListNode]) -> bool:
    q: Deque = collections.deque() # 데크 q 선언 및 초기화

    if not head: 
        return True 
    
    node = head 
    while node is not None: 
        q.append(node.val)
        node = node.next

    while len(q) > 1:
        if q.popleft() != q.pop():
            return False
        
    return True

# 런너를 이용한 풀이
def isPalindrome(self, head: Optional[ListNode]) -> bool:
    rev = None # 연결 리스트의 역순을 저장할 변수
    slow = fast = head # 두 개의 포인터 slow와 fast를 head로 초기화

    while fast and fast.next: # fast와 fast.next가 None이 아닐때 까지
        fast = fast.next.next # fast는 2칸씩 이동
        rev, rev.next, slow = slow, rev, slow.next # slow를 따라가며 역순으로 rev 구성
    if fast: # fast가 None이 아니라면, 연결 리스트의 길이가 홀수 이므로 slow를 한 칸 더 이동
        slow = slow.next

    while rev and rev.val == slow.val:
        slow, rev = slow.next, rev.next # rev와 slow의 값을 비교하여 팰린드롬 여부 확인
    return not rev # rev가 None이라면 팰린드롬이므로 True, 그렇지 않다면 False 반환