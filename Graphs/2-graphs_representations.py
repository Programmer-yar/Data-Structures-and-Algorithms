class Node():
	def __init__(self, value):
		self.value = value
		self.edges = []

class Edge():
	def __init__(self, value, node_from, node_to):
		self.value = value
		self.node_from = node_from
		self.node_to = node_to


class Graph():
	def __init__(self, nodes=[], edges=[]):
		self.nodes = nodes
		self.edges = edges

	def insert_node(self, new_node_val):
		new_node = Node(new_node_val)
		self.nodes.append(new_node)

	def insert_edge(self, new_edge_val, node_from_val, node_to_val):
		from_found = None
		to_found = None
		for node in self.nodes:
			if node_from_val == node.value:
				from_found = node
			if node_to_val == node.value:
				to_found = node

		if from_found == None:
			from_found = Node(node_from_val)
			self.nodes.append(from_found)
		if to_found == None:
			to_found = Node(node_to_val)
			self.nodes.append(to_found)
		new_edge = Edge(new_edge_val, from_found, to_found)
		from_found.edges.append(new_edge)
		to_found.edges.append(new_edge)
		self.edges.append(new_edge)

	def get_edge_list(self):
		edge_list = []
		for edge in self.edges:
			edge_list.append((edge.value, edge.node_from.value, edge.node_to.value))
		return edge_list

	def get_adjacency_list(self):
		"""
		The indecies of the outer list represent "from" nodes. Each section in the
		list will store a list of tuples that looks like this: (To Node, Edge Value)
        """
		nodes_value = [node.value for node in self.nodes]
		adjacency_list = [None] * (max(nodes_value)+1)

		for edge_object in self.edges:
			if adjacency_list[edge_object.node_from.value]:
				adjacency_list[edge_object.node_from.value].append((edge_object.node_to.value, edge_object.value))
			else:
				adjacency_list[edge_object.node_from.value] = [(edge_object.node_to.value, edge_object.value)]

		return adjacency_list

	def get_adjacency_matrix(self):
		"""Return a matrix, or 2D list.
		Row numbers represent from nodes,
		column numbers represent to nodes.
		Store the edge values in each spot,
		and a 0 if no edge exists."""
		nodes_value = [node.value for node in self.nodes]
		max_node = max(nodes_value) + 1
		adjacency_matrix = [[0]*max_node for i in range(max_node)]
		for edge_object in self.edges:
			adjacency_matrix[edge_object.node_from.value][edge_object.node_to.value] = edge_object.value
			
		return adjacency_matrix


graph = Graph()
graph.insert_edge(100, 1, 2)
graph.insert_edge(101, 1, 3)
graph.insert_edge(102, 1, 4)
graph.insert_edge(103, 3, 4)

print(graph.get_edge_list())
print(graph.get_adjacency_list())
print(graph.get_adjacency_matrix())
