"""
Chapter 04 - Problem 04 - 큐를 이용한 스택 구현 - https://leetcode.com/problems/implement-stack-using-queues/

문제 설명:
큐를 이용한 스택구현

예제:
Input
["MyStack", "push", "push", "top", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 2, 2, false]

Explanation
MyStack myStack = new MyStack();
myStack.push(1);
myStack.push(2);
myStack.top(); // return 2
myStack.pop(); // return 2
myStack.empty(); // return False

풀이:
push 메서드에서는 새로운 요소를 데크에 추가하고, 이전에 추가된 모든 요소를 한 칸씩 앞으로 이동시켜서 새로운 요소를 맨 앞에 위치시킵니다. 이렇게 하면 가장 먼저 추가된 요소가 스택의 
맨 위에 위치하게 됩니다. pop 메서드는 스택의 맨 위 요소를 데크에서 제거하고 반환합니다. top 메서드는 스택의 맨 위 요소를 반환하고, empty 메서드는 스택이 비어있는지 여부를 
확인하여 True 또는 False를 반환합니다.

"""

class MyStack:

    def __init__(self):
        self.q = collections.deque()  # 데크 (double-ended queue) 객체를 사용하여 스택 구현

    def push(self, x: int) -> None:
        self.q.append(x)  # 새로운 요소 x를 데크에 추가
        for _ in range(len(self.q)-1):  # 이전에 추가된 모든 요소를 한 칸씩 앞으로 이동하여 x를 맨 앞에 위치시킴
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        return self.q.popleft()  # 스택의 맨 앞 요소를 데크에서 제거하고 반환 (스택의 가장 위의 요소를 꺼냄)

    def top(self) -> int:
        return self.q[0]  # 스택의 맨 앞 요소를 반환 (스택의 가장 위의 요소를 확인)

    def empty(self) -> bool:
        return len(self.q) == 0  # 스택이 비어있는지 여부를 확인하여 True 또는 False를 반환