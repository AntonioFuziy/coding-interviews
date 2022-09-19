# DO NOT CHANGE THIS CLASS
class Stack:
  def __init__(self):
    self._items = []

  def push(self, value):
    self._items.append(value)

  def pop(self):
    return self._items.pop()

  def peek(self):
    return self._items[-1]

  def is_empty(self):
    return len(self) == 0

  def __len__(self):
    return len(self._items)


# IMPLEMENT YOUR SOLUTION HERE (DO NOT CHANGE THE ARGUMENTS)
def sort_stack(stack: Stack) -> None:
  stack2 = Stack()
  while not stack.is_empty():
    tmp = stack.pop()
    if stack2.is_empty():
      stack2.push(tmp)
    else:
      while not stack2.is_empty() and stack2.peek() > tmp:
        stack.push(stack2.pop())
      stack2.push(tmp)
  while not stack2.is_empty():
    stack.push(stack2.pop())
  
