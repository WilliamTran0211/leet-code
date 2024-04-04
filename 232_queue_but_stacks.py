# implement a queue using 2 stacks
class MyQueue(object):
    def __init__(self):
        self.name = None
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack1.append(x)

    def pop(self):
        """
        :rtype: int
        """
        res = None
        while len(self.stack1) > 0:
            res = self.stack1.pop()
            self.stack2.append(res)

        while len(self.stack2) > 0:
            tmp = self.stack2.pop()
            if tmp != res:
                self.stack1.append(tmp)

        print(self.stack1, self.stack2, res)
        return res

    def peek(self):
        """
        :rtype: int
        """
        return self.stack1[0]

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.stack1) == 0 and len(self.stack2) == 0


myQueue = MyQueue()
myQueue.push(1)
myQueue.push(2)
myQueue.push(3)
myQueue.push(4)
print(myQueue.peek())
myQueue.pop()
print(myQueue.empty())
print(myQueue.peek())
myQueue.pop()
print(myQueue.empty())
