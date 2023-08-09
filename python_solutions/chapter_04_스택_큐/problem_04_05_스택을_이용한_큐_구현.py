"""
Chapter 04 - Problem 05 - 스택을 이용한 큐 구현 - https://leetcode.com/problems/implement-queue-using-stacks/

문제 설명:
- push(x): 요소 x를 큐 마지막에 삽입한다.
- pop(): 큐 처음에 있는 요소를 제거한다.
- peek(): 큐 처음에 있는 요소를 조회한다.
- empty(): 큐가 비어 있는지 여부를 리턴한다.
예제:
Input
["MyQueue", "push", "push", "peek", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 1, 1, false]

Explanation
MyQueue myQueue = new MyQueue();
myQueue.push(1); // queue is: [1]
myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
myQueue.peek(); // return 1
myQueue.pop(); // return 1, queue is [2]
myQueue.empty(); // return false

풀이:
input 스택은 요소를 삽입할 때 사용되며, output 스택은 출력작업(peek와 pop)을 위해 사용됩니다. pop 및 peek 함수내에서 출력용 스택(output)이 비어있다면, 입력용 스(input)의 요소들을 역순으로 출력용 스택으로 옮기는 작업을 수행하고, 그 후에 요소를 처리합니다.

"""
class MyQueue:
    def __init__(self):
        self.input = []
        self.output = []
    
    def push(self, x):
        self.input.append(x)

    def pop(self):
        self.peek()
        return self.output.pop()
    
    def peek(self):
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]
    
    def empty(self):
        return self.input == [] and self.output == []