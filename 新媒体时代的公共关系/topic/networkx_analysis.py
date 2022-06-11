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
nodes_dict = {}

for i in range(len(df_nodes)):
    nodes.append(df_nodes['Id'][i])
    nodes_dict[df_nodes['Id'][i]] = df_nodes['Label'][i]

# edges
df_edges = pd.read_csv('topic/edges_3.csv')
edges = []

for i in range(len(df_edges)):
    edges.append(
        (df_edges['Source'][i],
         df_edges['Target'][i])
    )

G = nx.DiGraph()
G.add_nodes_from(nodes)
G.add_edges_from(edges)

n = len(nodes)
m = len(edges)

indegree = G.in_degree()
indegree_dict = {}
for ind in indegree:
    indegree_dict[nodes_dict[ind[0]]] = ind[1]

tuples =  sorted(indegree_dict.items(), key=lambda d:d[1], reverse = True)
print(tuples)

outdegree = G.out_degree()
outdegree_dict = {}
for out in outdegree:
    outdegree_dict[nodes_dict[out[0]]] = out[1]

tuples =  sorted(outdegree_dict.items(), key=lambda d:d[1], reverse = True)
print(tuples)

print('网络的节点个数',n)
print('网络的边个数',m)

print(nx.betweenness_centrality(G))
print('网络的密度',m / (n * (n - 1) / 2))
print('网络的聚类系数',nx.average_clustering(G))
print('网络的平均距离',nx.degree_centrality(G))



# matrix = nx.adj_matrix(G).todense()
# from sklearn.cluster import SpectralClustering
# sc = SpectralClustering(affinity='precomputed', n_init=100,assign_labels='discretize')
# new = sc.fit_predict(matrix)
# print(list(new))

# 点个数
# 边个数
# 整体网络的密度
# 点度中心性分析
#     - 点入度
#     - 点出度
#     - 转发关系单向化