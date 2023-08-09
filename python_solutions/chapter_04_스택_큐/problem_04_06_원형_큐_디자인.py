"""
Chapter 04 - Problem 06 - 원형 큐 디자인 - https://leetcode.com/problems/design-circular-queue/ 

문제 설명:
원형 큐를 디자인 하라
MyCircularQueue myCircularQueue = new MyCircularQueue(3); 
myCircularQueue.enQueue(1); // return True
myCircularQueue.enQueue(2); // return True
myCircularQueue.enQueue(3); // return True
myCircularQueue.enQueue(4); // return False
myCircularQueue.Rear();     // return 3
myCircularQueue.isFull();   // return True
myCircularQueue.deQueue();  // return True
myCircularQueue.enQueue(4); // return True
myCircularQueue.Rear();     // return 4

풀이:
원형 큐는 선형 큐와 달리 마지막 요소 다음에 첫 번째 요소가 오는 구조로 이루어져 있습니다. 따라서 인덱스를 원형으로 순환하며 큐의 요소를 저장하고 처리해야 합니다. 원형 큐를 디자인하기 위해서는 Front 포인터와 Rear 포인터를 조작하면서 원형으로 데이터를 저장하고 관리해야 합니다. 

"""

class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [None] * k
        self.maxlen = k
        self.p1 = 0 # Front 포인터
        self.p2 = 0 # Rear 포인터

    def enQueue(self, value: int) -> bool:
        if self.q[self.p2] is None: # Rear 포인터에 요소가 없는 경우
            self.q[self.p2] = value # 값을 삽입
            self.p2 = (self.p2 + 1) % self.maxlen # Rear 포인터 이동
            return True
        else:
            return False

    def deQueue(self) -> bool:
        if self.q[self.p1] is None: # Front 포인터에 요소가 없는 경우
            return False
        else:
            self.q[self.p1] = None  # Front 포인터의 값을 삭제 처리
            self.p1 = (self.p1 + 1) % self.maxlen # Front 포인터 이동
            return True
    def Front(self) -> int:
        return -1 if self.q[self.p1] is None else self.q[self.p1] # Front 포인터가 가리키는 요소 반환

    def Rear(self) -> int:
        return -1 if self.q[self.p2 - 1] is None else self.q[self.p2 - 1]  # Rear 포인터 바로 앞의 요소 반환

    def isEmpty(self) -> bool:
        return self.p1 == self.p2 and self.q[self.p1] is None  # Front와 Rear 포인터가 같고 값이 없는 경우 비어있다고 판단

    def isFull(self) -> bool:
        return self.p1 == self.p2 and self.q[self.p1] is not None  # Front와 Rear 포인터가 같고 값이 있는 경우 가득 차있다고 판단

