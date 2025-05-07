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

def walk(tree, stack):
	if tree is not None:
		stack.append(tree)
	while stack:
		node = stack.pop()
		if node:
			print(node)
			stack.append(node.right)
			stack.append(node.left)

stack = []
print("Enter the binary tree in pre-order format (value, then left subtree, then right subtree):")
root = build_tree()
walk(root, stack)
