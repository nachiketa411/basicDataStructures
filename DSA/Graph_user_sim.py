from Graph import Graph
import networkx as nx
import matplotlib.pyplot as plt

def visualize_graph(graph):
    G = nx.DiGraph() if graph.is_directed else nx.Graph()

    for edge in graph.edges:
        G.add_edge(graph.node_names[edge.node_from.value], graph.node_names[edge.node_to.value], weight=edge.value)

    pos = nx.spring_layout(G)
    edge_labels = {(graph.node_names[edge.node_from.value], graph.node_names[edge.node_to.value]): edge.value for edge in graph.edges}
    nx.draw(G, pos, with_labels=True, node_size=3000, node_color="skyblue", font_size=15, font_weight="bold", arrows=True if graph.is_directed else False)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=12)
    plt.show()

def main():
    # Get user input for graph type
    graph_type = input("Enter graph type (directed/undirected): ").strip().lower()
    is_directed = graph_type == 'directed'

    # Create a graph instance
    graph = Graph(is_directed)

    # Get user input for node names
    node_names = input("Enter node names separated by commas: ").strip().split(',')
    graph.set_node_names(node_names)

    # Get user input for edges
    print("Enter edges in the format 'from,to,value' (one per line). Enter 'done' when finished:")
    while True:
        edge_input = input().strip()
        if edge_input.lower() == 'done':
            break
        from_node, to_node, value = edge_input.split(',')
        graph.insert_edge(int(value), node_names.index(from_node), node_names.index(to_node))

    # Get user input for start node for traversal
    start_node_name = input("Enter start node for traversal: ").strip()
    start_node_num = node_names.index(start_node_name)

    # Perform DFS and BFS
    print("DFS:", graph.dfs_names(start_node_num))
    print("BFS:", graph.bfs_names(start_node_num))

    # Visualize the graph
    visualize_graph(graph)

if __name__ == "__main__":
    main()