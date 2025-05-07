from collections import deque

class Node:
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right
	def __str__(self):
		return "Node(" + str(self.value) + ")"

def build_tree():
	value = input("Enter node value (or leave empty for None): ")
	if value == "":
		return None
	left = build_tree()
	right = build_tree()
	return Node(value, left, right)

def bfs(tree):
	if not tree:
		return
	queue = deque()
	queue.append(tree)
	while queue:
		node = queue.popleft()
		print(node)
		if node.left:
			queue.append(node.left)
		if node.right:
			queue.append(node.right)

print("Enter the binary tree in pre-order format (value, then left subtree, then right subtree):")
root = build_tree()
print("\nBreadth-First Search (Level-order) Traversal:")
bfs(root)
