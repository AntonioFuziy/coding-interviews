class Node:
  def __init__(self, value, nxt=None):
    self.value = value
    self.next = nxt

def find_intersection(head1: Node, head2: Node) -> Node:
  if not head1 or not head2:
    return None
  
  size1 = 0
  size2 = 0
  
  curr1 = head1
  curr2 = head2
  
  while curr1 is not None:
    curr1 = curr1.next
    size1 += 1
  
  while curr2 is not None:
    curr2 = curr2.next
    size2 += 1
  
  if size1 > size2:
    for _ in range(size1 - size2):
      head1 = head1.next
  else:
    for _ in range(size2 - size1):
      head2 = head2.next
    
  while head1 is not None and head2 is not None:
    if head1 == head2:
      return head1
    head1 = head1.next
    head2 = head2.next
  return None