class Stack:
    def __init__(self, items=None, limit=100):
        self.items = items if items is not None else []
        self.limit = limit

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        if len(self.items) >= self.limit:
            raise OverflowError("Stack limit reached. Cannot push any more items.")
        self.items.append(item)

    def pop(self):
        if self.isEmpty():
            raise IndexError("Pop from an empty stack")
        return self.items.pop()

    def peek(self):
        if self.isEmpty():
            raise IndexError("Peek from an empty stack")
        return self.items[-1]

    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items) >= self.limit

    def search(self, target):
        try:
            # Return the distance from the top of the stack
            return len(self.items) - 1 - self.items[::-1].index(target)
        except ValueError:
            return -1

    def __repr__(self):
        return f"Stack({self.items}, limit={self.limit})"
