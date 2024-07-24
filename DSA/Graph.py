from collections import defaultdict, deque

class Node:
    def __init__(self, value):
        self.value = value
        self.edges = []
        self.visited = False

class Edge:
    def __init__(self, value, node_from, node_to):
        self.value = value
        self.node_from = node_from
        self.node_to = node_to

class Graph:
    def __init__(self, is_directed=True):
        self.nodes = []
        self.edges = []
        self.node_names = []
        self._node_map = {}
        self.is_directed = is_directed

    def set_node_names(self, names):
        """Set names for nodes where the ith name in names corresponds to node number i."""
        self.node_names = list(names)

    def insert_node(self, new_node_val):
        """Insert a new node with value new_node_val."""
        if new_node_val not in self._node_map:
            new_node = Node(new_node_val)
            self.nodes.append(new_node)
            self._node_map[new_node_val] = new_node
        return self._node_map[new_node_val]

    def insert_edge(self, new_edge_val, node_from_val, node_to_val):
        """Insert a new edge, creating new nodes if necessary."""
        node_from = self.insert_node(node_from_val)
        node_to = self.insert_node(node_to_val)
        new_edge = Edge(new_edge_val, node_from, node_to)
        node_from.edges.append(new_edge)
        if not self.is_directed:
            # Add reverse edge for undirected graph
            reverse_edge = Edge(new_edge_val, node_to, node_from)
            node_to.edges.append(reverse_edge)
            self.edges.append(reverse_edge)
        self.edges.append(new_edge)

    def get_edge_list(self):
        """Return a list of triples (Edge Value, From Node, To Node)."""
        return [(e.value, e.node_from.value, e.node_to.value) for e in self.edges]

    def get_edge_list_names(self):
        """Return a list of triples (Edge Value, From Node Name, To Node Name)."""
        return [(e.value, self.node_names[e.node_from.value], self.node_names[e.node_to.value]) for e in self.edges]

    def get_adjacency_list(self):
        """Return a list of lists where indices represent "from" nodes and each list contains tuples (To Node, Edge Value)."""
        adjacency_list = defaultdict(list)
        for e in self.edges:
            adjacency_list[e.node_from.value].append((e.node_to.value, e.value))
        return [adjacency_list[i] or None for i in range(len(self.node_names))]

    def get_adjacency_list_names(self):
        """Return a list of lists where indices represent "from" nodes and each list contains tuples (To Node Name, Edge Value)."""
        adjacency_list = self.get_adjacency_list()
        return [[(self.node_names[to], val) for to, val in adj] if adj else None for adj in adjacency_list]

    def get_adjacency_matrix(self):
        """Return a matrix where rows represent "from" nodes, columns represent "to" nodes, and values are edge values or 0 if no edge exists."""
        size = len(self.node_names)
        adjacency_matrix = [[0] * size for _ in range(size)]
        for e in self.edges:
            adjacency_matrix[e.node_from.value][e.node_to.value] = e.value
        return adjacency_matrix

    def find_node(self, node_number):
        """Return the node with value node_number or None."""
        return self._node_map.get(node_number)
    
    def _clear_visited(self):
        for node in self.nodes:
            node.visited = False

    def dfs_helper(self, start_node):
        """Recursive helper for Depth First Search."""
        start_node.visited = True
        ret_list = [start_node.value]
        for e in start_node.edges:
            if not e.node_to.visited:
                ret_list.extend(self.dfs_helper(e.node_to))
        return ret_list

    def dfs(self, start_node_num):
        """Perform Depth First Search starting from start_node_num."""
        self._clear_visited()
        start_node = self.find_node(start_node_num)
        if start_node is None:
            return []  # Return an empty list if the start node does not exist
        return self.dfs_helper(start_node)

    def dfs_names(self, start_node_num):
        """Return DFS result with node names instead of numbers."""
        return [self.node_names[num] for num in self.dfs(start_node_num)]

    def bfs(self, start_node_num):
        """Perform Breadth First Search starting from start_node_num."""
        start_node = self.find_node(start_node_num)
        if start_node is None:
            return []  # Return an empty list if the start node does not exist
        self._clear_visited()
        ret_list = []
        queue = deque([start_node])
        start_node.visited = True
        while queue:
            node = queue.popleft()
            ret_list.append(node.value)
            for e in node.edges:
                if not e.node_to.visited:
                    e.node_to.visited = True
                    queue.append(e.node_to)
        return ret_list

    def bfs_names(self, start_node_num):
        """Return BFS result with node names instead of numbers."""
        return [self.node_names[num] for num in self.bfs(start_node_num)]
