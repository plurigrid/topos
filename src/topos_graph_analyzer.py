import os
import networkx as nx
from typing import Dict, List, Tuple
import matplotlib.pyplot as plt
from networkx.algorithms import community
import numpy as np
import textwrap
from networkx.algorithms import community
import numpy as np
import textwrap

def ascii_tree(graph: nx.DiGraph, root: str, indent: str = '', is_last: bool = True) -> str:
    """Generate an ASCII tree representation of the graph structure."""
    tree = indent
    if root != '':
        tree += '└── ' if is_last else '├── '
        tree += os.path.basename(root) + '\n'
        indent += '    ' if is_last else '│   '

    children = list(graph.successors(root))
    for i, child in enumerate(children):
        tree += ascii_tree(graph, child, indent, i == len(children) - 1)
    
    return tree

def ascii_graph(graph: nx.DiGraph) -> str:
    """Generate a simple ASCII graph representation."""
    ascii_rep = "Graph Structure:\n"
    ascii_rep += "  ___________\n"
    ascii_rep += " /           \\\n"
    ascii_rep += "| Nodes: {:4d} |\n".format(graph.number_of_nodes())
    ascii_rep += "| Edges: {:4d} |\n".format(graph.number_of_edges())
    ascii_rep += " \\___________/\n"
    return ascii_rep

def ascii_communities(communities: List[List[str]]) -> str:
    """Generate an ASCII representation of communities."""
    ascii_rep = "Communities:\n"
    for i, community in enumerate(communities):
        ascii_rep += f"Community {i+1}: {len(community)} nodes\n"
        ascii_rep += "  ____________________________\n"
        ascii_rep += " /                            \\\n"
        for node in community[:3]:
            ascii_rep += f"| {textwrap.shorten(node, width=26):26} |\n"
        if len(community) > 3:
            ascii_rep += "|            ...             |\n"
        ascii_rep += " \\____________________________/\n\n"
    return ascii_rep

def analyze_topos_directory(root_dir: str = '/Users/barton/topos') -> nx.DiGraph:
    """
    Analyze the topos directory and create a reflexive evolving graph structure.
    
    :param root_dir: The root directory to start the analysis
    :return: A NetworkX DiGraph representing the directory structure
    """
    graph = nx.DiGraph()
    
    for root, dirs, files in os.walk(root_dir):
        level = root.replace(root_dir, '').count(os.sep)
        parent = os.path.dirname(root)
        
        # Add node for current directory with interpolated subtext
        graph.add_node(root, type='directory', level=level, subtext=interpolate_subtext(root))
        
        # Add edge from parent to current directory
        if parent != root:
            graph.add_edge(parent, root, superstructure=extrapolate_superstructure(f"{parent}->{root}"))
        
        # Add nodes for files
        for file in files:
            file_path = os.path.join(root, file)
            graph.add_node(file_path, type='file', level=level+1, subtext=interpolate_subtext(file))
            graph.add_edge(root, file_path, superstructure=extrapolate_superstructure(f"{root}->{file}"))
        
        # Add reflexive edges
        graph.add_edge(root, root, superstructure=extrapolate_superstructure(f"{root}->{root}"))
    
    return graph

def interpolate_subtext(text: str) -> str:
    """Interpolate subtext within a string."""
    return ''.join([f"{c}[{ord(c)}]" for c in text])

def extrapolate_superstructure(text: str) -> str:
    """Extrapolate superstructure from a string."""
    return f"[{len(text)}]{text.upper()}[{sum(ord(c) for c in text)}]"

def analyze_osi_levels(graph: nx.DiGraph) -> Dict[int, List[str]]:
    """
    Analyze the OSI levels in the graph structure.
    
    :param graph: The NetworkX DiGraph representing the directory structure
    :return: A dictionary mapping OSI levels to lists of nodes
    """
    osi_levels = {}
    for node, data in graph.nodes(data=True):
        level = data.get('level', 0)
        if level not in osi_levels:
            osi_levels[level] = []
        osi_levels[level].append(node)
    return osi_levels

def assess_visibility(graph: nx.DiGraph) -> float:
    """
    Assess the visibility or clarity of the project structure.
    
    :param graph: The NetworkX DiGraph representing the directory structure
    :return: A score between 0 and 1 indicating the visibility (1 being perfectly clear)
    """
    total_nodes = graph.number_of_nodes()
    total_edges = graph.number_of_edges()
    max_depth = max(data['level'] for _, data in graph.nodes(data=True))
    
    # Calculate visibility score based on various factors
    depth_score = 1 / (1 + max_depth)  # Lower depth is better
    connectivity_score = min(total_edges / (total_nodes * 2), 1)  # More connections up to a point
    symmetry_score = 1 - (abs(graph.number_of_edges() - graph.number_of_nodes()) / max(graph.number_of_edges(), graph.number_of_nodes()))
    
    visibility_score = (depth_score + connectivity_score + symmetry_score) / 3
    return visibility_score

def detect_communities(graph: nx.DiGraph) -> List[List[str]]:
    """
    Detect communities in the graph using the Louvain method.
    
    :param graph: The NetworkX DiGraph representing the directory structure
    :return: A list of communities, where each community is a list of node names
    """
    undirected_graph = graph.to_undirected()
    communities = community.louvain_communities(undirected_graph)
    return [list(comm) for comm in communities]

def visualize_graph(graph: nx.DiGraph, communities: List[List[str]]):
    """
    Visualize the graph with community colors and save in multiple formats.
    
    :param graph: The NetworkX DiGraph representing the directory structure
    :param communities: A list of communities, where each community is a list of node names
    """
    pos = nx.spring_layout(graph)
    plt.figure(figsize=(12, 8))
    
    colors = plt.cm.rainbow(np.linspace(0, 1, len(communities)))
    for i, comm in enumerate(communities):
        nx.draw_networkx_nodes(graph, pos, nodelist=comm, node_color=[colors[i]], node_size=100, alpha=0.8)
    
    nx.draw_networkx_edges(graph, pos, alpha=0.5, arrows=True)
    nx.draw_networkx_labels(graph, pos, {node: node.split('/')[-1] for node in graph.nodes()}, font_size=8)
    
    plt.title("Topos Directory Structure with Communities")
    plt.axis('off')
    plt.tight_layout()
    
    # Save in multiple formats
    for format in ['png', 'svg', 'pdf']:
        plt.savefig(f"topos_graph.{format}", dpi=300, bbox_inches='tight')
    
    plt.close()

def main():
    graph = analyze_topos_directory()
    osi_levels = analyze_osi_levels(graph)
    visibility_score = assess_visibility(graph)
    communities = detect_communities(graph)
    
    print(ascii_graph(graph))
    
    print("Reflexive Evolving Graph Structure:")
    print(ascii_tree(graph, '/Users/barton/topos'))
    
    print("\nOSI Levels:")
    for level, nodes in osi_levels.items():
        print(f"Level {level}:")
        for node in nodes[:3]:  # Print first 3 nodes of each level
            print(f"  - {node}")
        if len(nodes) > 3:
            print("  ...")
    
    print(f"\nVisibility Score: {visibility_score:.2f}")
    print(f"We can see the project structure with {visibility_score*100:.2f}% clarity.")
    
    print(ascii_communities(communities))
    
    visualize_graph(graph, communities)
    print("\nGraph visualizations saved as 'topos_graph.png', 'topos_graph.svg', and 'topos_graph.pdf'")

if __name__ == "__main__":
    main()
