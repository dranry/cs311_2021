#Goal: Make a tree of nodes to be the basis for an artificial neural network
import random
import string
import itertools

NODE_COUNT_PER_LAYER = [4,3,2]
class Node:
	def __init__(self):
		self.weight = []
		self.children = []
		self.node_name = ''
		random_letters = [] 
		for i in range(3):
			random_letters.append(random.choice(string.ascii_letters))
		self.node_name = ''.join(random_letters)
	
	def make_children(self, current_layer_number, node_per_layer_map):
		if current_layer_number >= len(node_per_layer_map):
			return

		for i in range(node_per_layer_map[current_layer_number]):
			self.children.append(Node())
	
		self.children[0].make_children(current_layer_number + 1, node_per_layer_map)

		for i in range(1, len(self.children)):
			self.children[i].children = self.children[0].children[:]

	def pretty_print(self, current_layer_number, node_per_layer_map):
		indent = '	' * current_layer_number

		if current_layer_number >= len(node_per_layer_map):
			print(f"{indent} {self.node_name}")
			return

		print(f"{indent} {self.node_name} is connected to")
		for i in range(len(self.children)):
			try:
				print(f"{indent} with weight of {self.weight[i]}")
			except:
				pass
			self.children[i].pretty_print(current_layer_number + 1, node_per_layer_map)
		return

	def set_random_weights(self, current_layer_number, node_per_layer_map):
		if current_layer_number >= len(node_per_layer_map):
			return

		self.weight = [0.0] * len(self.children)
			
		for i in range(len(self.children)):
			self.weight[i] = random.uniform(0, 1)
			self.children[i].set_random_weights(current_layer_number + 1, node_per_layer_map)			
		return

new_node = Node()
new_node.make_children(0, NODE_COUNT_PER_LAYER)
print("Without Weights!!")
new_node.pretty_print(0, NODE_COUNT_PER_LAYER)
new_node.set_random_weights(0, NODE_COUNT_PER_LAYER)
print("\nWith Weights!!\n")
new_node.pretty_print(0, NODE_COUNT_PER_LAYER)
