import json
import pandas as pd
import numpy
import networkx as nx
import community as community_louvain
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np



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

n = len(nodes)
m = len(edges)


# print('网络的密度',m / (n * (n - 1) / 2))
# print('网络的聚类系数',nx.average_clustering(G))
# print('网络的平均距离',nx.degree_centrality(G))

matrix = nx.adj_matrix(G).todense()
from sklearn.cluster import SpectralClustering
sc = SpectralClustering(affinity='precomputed', n_init=100,assign_labels='discretize')
new = sc.fit_predict(matrix)
print(list(new))

# newG = nx.k_core(G,k=2)
# print(newG.nodes())
# print(newG.edges())
# print(len(newG.nodes))
# print(len(newG.edges))