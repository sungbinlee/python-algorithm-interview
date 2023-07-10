"""
Chapter 03 - Problem 04 - 두 수의 덧셈 - https://leetcode.com/problems/add-two-numbers/

문제 설명:

예제:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

풀이1: 
전가산기 구현
이 풀이에서는 주어진 두 연결 리스트 l1과 l2를 순회하면서 각 자릿수의 합을 계산합니다. 
각 노드의 값을 가져와 더한 뒤, 이전에 발생한 올림 값을 함께 더합니다. 그리고 나서 현재 
자릿수의 값과 올림 값을 가지는 새로운 노드를 생성하고, 포인터를 다음 노드로 이동시킵니다.

더이상 순회할 노드가 없을 때까지 반복하며 합을 계산한 후, 마지막으로 올림 값이 발생한 
경우에는 새로운 노드로 추가합니다.

마지막으로, 더미(dummy) 노드의 다음 노드를 반환하여 결과로 나오는 연결 리스트의 헤드 노드를 얻습니다.

"""

def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    # 결과로 반환할 연결 리스트의 가상 노드(dummy node)를 생성합니다.
    dummy = ListNode(0)
    # 현재 노드를 가리키기 위한 포인터를 생성합니다.
    current = dummy
    # 올림(carry) 값을 저장하기 위한 변수를 초기화합니다.
    carry = 0

    # l1과 l2의 노드를 순회합니다. 두 리스트 중 하나라도 끝에 도달할 때까지 반복합니다.
    while l1 or l2:
        # sum_val 변수에 현재 올림 값을 저장합니다.
        sum_val = carry
        # l1이 None이 아닌지 확인합니다.
        if l1:
            # l1의 값(sum_val)을 sum_val에 더합니다.
            sum_val += l1.val
            # l1을 다음 노드로 이동합니다.
            l1 = l1.next
        # l2가 None이 아닌지 확인합니다.
        if l2:
            # l2의 값(sum_val)을 sum_val에 더합니다.
            sum_val += l2.val
            # l2를 다음 노드로 이동합니다.
            l2 = l2.next
        # sum_val을 10으로 나눈 몫을 carry에 저장합니다.
        carry = sum_val // 10
        # sum_val을 10으로 나눈 나머지를 가지는 새로운 노드를 생성합니다.
        current.next = ListNode(sum_val % 10)
        # current를 다음 노드로 이동합니다.
        current = current.next
    # 만약 carry 값이 0보다 크다면, 추가적인 노드를 생성하여 carry를 표현합니다.
    if carry > 0:
        current.next = ListNode(carry)
    # 가상 노드(dummy node)의 다음 노드를 반환합니다. 이는 두 입력 리스트의 합을 나타내는 실제 헤드 노드입니다.
    return dummy.next
