# Case Study: Metro Route Planning in Metropolis
# The city of Gotham has built a small-scale metro network to connect key areas. Each zone is represented as
# a vertex, and a direct metro connection between two zones is represented as an unweighted edge (ignoring
# travel time or distance).
# Zones and Labels
# – A: Central Station
# – B: North Market
# – C: East Residential
# – D: South Tech Park
# – E: University Circle
# – F: Airport Terminal
# Edge connections
# – A is connected to B and C
# – B is connected to D
# – C is connected to D and E
# – D is connected to E and F
# – E is connected to F
# Tasks
# 1. Draw the pictorial description of the graph. Also, construct the adjacency matrix.
# 2. Store the adjacency matrix using numpy.
# 3. Write a Python code to determine the number of paths that are exactly three edges long, connecting
# the vertices A and F.
# 4. Using Depth-First Search (DFS), list all the zones (vertices) reachable from the Central Station (A).
# Show the DFS traversal sequence. [Use alphabetical order to choose the vertex.] Write the Python code for it.

import numpy as np
import pandas as pd
adj = np.array([
    [0, 1, 1, 0, 0, 0],  # A
    [1, 0, 0, 1, 0, 0],  # B
    [1, 0, 0, 1, 1, 0],  # C
    [0, 1, 1, 0, 1, 1],  # D
    [0, 0, 1, 1, 0, 1],  # E
    [0, 0, 0, 1, 1, 0]   # F
])

vertex_map = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5}
paths_len3 = np.linalg.matrix_power(adj, 3)[vertex_map['A'], vertex_map['F']]

def dfs(start, adj):
    visited, stack, seq = set(), [start], []
    while stack:
        v = stack.pop()
        if v not in visited:
            visited.add(v)
            seq.append(v)
            stack.extend(sorted(np.where(adj[v])[0])[::-1])
    return [chr(65 + i) for i in seq]

print("Number of paths from A to F (exactly 3 edges):", paths_len3)
labels = ['A', 'B', 'C', 'D', 'E', 'F']
adj_df = pd.DataFrame(adj, index=labels, columns=labels)
print("Adjacency Matrix (A-F):\n", adj_df)
print("Number of paths from A to F with exactly three edges:", paths_len3)
print("DFS Traversal Sequence starting from A:", dfs(0, adj))
