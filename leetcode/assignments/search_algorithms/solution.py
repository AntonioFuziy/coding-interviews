# Do not modify the classes below
class TreeNode:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None


class Tree:
    def __init__(self, representation: str):
        '''
        representation: list of values representing a binary tree. The left and right
        children of the ith element are 2i+1 and 2i+2, respectively.
        '''
        if not representation:
            return
        nodes = []
        for i, value in enumerate(representation):
            node = None
            if value is not None:
                node = TreeNode(value)
                if i > 0:
                    if i % 2 == 1:
                        parent = nodes[(i - 1) // 2]
                        parent.left = node
                    else:
                        parent = nodes[(i - 2) // 2]
                        parent.right = node
            nodes.append(node)
        self.root = nodes[0]


class GraphNode:
    def __init__(self, value=None):
        self.value = value
        self.adjacent = []


class Graph:
    def __init__(self, adjacency: list[list[bool]]):
        '''
        adjacency: list of values representing a binary tree. The left and right
        children of the ith element are 2i+1 and 2i+2, respectively.
        '''
        self.nodes = [GraphNode(i) for i in range(1, len(adjacency) + 1)]
        for node1, row in zip(self.nodes, adjacency):
            for node2, adjacent in zip(self.nodes, row):
                if adjacent and node1 is not node2:
                    node1.adjacent.append(node2)


# Implement the functions below

def pre_order_recursive(root: TreeNode) -> None:
    if root.value is None:
        return
    print(root.value)

    if root.left:
        pre_order_recursive(root.left)
    if root.right:
        pre_order_recursive(root.right) 

def pre_order_iterative(root: TreeNode) -> None:
    stack = []
    stack.append(root)
    while stack:
        current = stack.pop()
        print(current.value)
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
    

def in_order_recursive(root: TreeNode) -> None:
    if root.value is None:
        return
    if root.left:
        in_order_recursive(root.left)
    print(root.value)
    if root.right:
        in_order_recursive(root.right)


def post_order_recursive(root: TreeNode) -> None:
    if root.value is None:
        return
    if root.left:
        post_order_recursive(root.left)
    if root.right:
        post_order_recursive(root.right)
    print(root.value)


def breadth_first(root: TreeNode) -> None:
    queue = []
    queue.append(root)
    while queue:
        current = queue.pop(0)
        print(current.value)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    

def graph_depth_first_recursive(node: GraphNode, visited=None) -> None:
    if visited is None:
        visited = set()
    if node.value in visited:
        return
    visited.add(node.value)
    print(node.value)
    for adj in node.adjacent:
        graph_depth_first_recursive(adj, visited)


def graph_depth_first_iterative(node: GraphNode) -> None:
    if node.value is None:
        return
    stack = []
    stack.append(node)
    visited = set()
    while stack:
        current = stack.pop()
        if current.value in visited:
            continue
        visited.add(current.value)
        print(current.value)
        for adj in current.adjacent:
            stack.append(adj)


def graph_breadth_first(node: GraphNode) -> None:
    if node.value is None:
        return
    queue = []
    queue.append(node)
    visited = set()
    while queue:
        current = queue.pop(0)
        if current.value in visited:
            continue
        visited.add(current.value)
        print(current.value)
        for adj in current.adjacent:
            queue.append(adj)