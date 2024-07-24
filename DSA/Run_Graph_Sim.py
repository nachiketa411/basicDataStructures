from Graph import Graph
def run_simulations(directed):
    # Create a new graph
    graph = Graph(is_directed=directed)
    # graph = Graph(is_directed=False)

    # Set node names (optional)
    graph.set_node_names(['A', 'B', 'C', 'D', 'E'])

    # Insert nodes and edges
    graph.insert_node(0)
    graph.insert_node(1)
    graph.insert_node(2)
    graph.insert_node(3)
    graph.insert_node(4)


    # (edge_value, node_from, node_to)
    graph.insert_edge(1, 0, 1)
    graph.insert_edge(2, 0, 2)
    graph.insert_edge(3, 1, 2)
    graph.insert_edge(4, 1, 3)
    graph.insert_edge(5, 2, 4)
    graph.insert_edge(6, 3, 4)

    # Print edge list
    print("Edge List:", graph.get_edge_list())
    print("Edge List with Names:", graph.get_edge_list_names())

    # Print adjacency list
    print("Adjacency List:", graph.get_adjacency_list())
    print("Adjacency List with Names:", graph.get_adjacency_list_names())

    # Print adjacency matrix
    print("Adjacency Matrix:")
    matrix = graph.get_adjacency_matrix()
    for row in matrix:
        print(row)

    # Perform DFS and BFS
    print("DFS from node 2:", graph.dfs(2))
    print("DFS from node 2 with names:", graph.dfs_names(2))

    print("BFS from node 2:", graph.bfs(2))
    print("BFS from node 2 with names:", graph.bfs_names(2))

# Run the simulations
print('-----------------------------')
print('Directed Graph')
print('-----------------------------')
run_simulations(directed=True)
print('-----------------------------')
print('Undirected/Bidirectional Graph')
print('-----------------------------')
run_simulations(directed=False)


# getUserInput
# Get graph visualizations
