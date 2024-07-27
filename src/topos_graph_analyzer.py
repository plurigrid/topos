import os
import networkx as nx
from typing import Dict, List

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
        
        # Add node for current directory
        graph.add_node(root, type='directory', level=level)
        
        # Add edge from parent to current directory
        if parent != root:
            graph.add_edge(parent, root)
        
        # Add nodes for files
        for file in files:
            file_path = os.path.join(root, file)
            graph.add_node(file_path, type='file', level=level+1)
            graph.add_edge(root, file_path)
        
        # Add reflexive edges
        graph.add_edge(root, root)
    
    return graph

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

def main():
    graph = analyze_topos_directory()
    osi_levels = analyze_osi_levels(graph)
    visibility_score = assess_visibility(graph)
    
    print("Reflexive Evolving Graph Structure:")
    for node, degree in graph.degree():
        print(f"Node: {node}, Connections: {degree}")
    
    print("\nOSI Levels:")
    for level, nodes in osi_levels.items():
        print(f"Level {level}:")
        for node in nodes:
            print(f"  - {node}")
    
    print(f"\nVisibility Score: {visibility_score:.2f}")
    print(f"We can see the project structure with {visibility_score*100:.2f}% clarity.")

if __name__ == "__main__":
    main()
