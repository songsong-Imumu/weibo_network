import json
import pandas as pd
import numpy
import networkx as nx
import community as community_louvain
import matplotlib.pyplot as plt
import matplotlib.cm as cm



# nodes
df_nodes = pd.read_csv('topic/nodes_3.csv')
nodes = []

for i in range(len(df_nodes)):
    nodes.append(df_nodes['Id'][i])

# edges
df_edges = pd.read_csv('topic/edges_3.csv')
edges = []

for i in range(len(df_edges)):
    edges.append(
        (df_edges['Source'][i],
         df_edges['Target'][i])
    )

G = nx.Graph()
G.add_nodes_from(nodes)
G.add_edges_from(edges)


# print(partition)

# pos = nx.spring_layout(G)

# cmap = cm.get_cmap('viridis', max(partition.values()) + 1)
# nx.draw_networkx_nodes(G, pos, partition.keys(), node_size=40,
                       # cmap=cmap, node_color=list(partition.values()))
# nx.draw_networkx_edges(G, pos, alpha=0.5)
# plt.show()

largest = max(nx.connected_components(G),key=len)
largest_connected_subgraph = G.subgraph(largest)

partition = community_louvain.best_partition(largest_connected_subgraph)
print(partition)
