import json
import pandas as pd
import numpy
import networkx as nx

# nodes
df_nodes = pd.read_csv('topic/nodes_3.csv')
d3_nodes = []
nodes = []

for i in range(len(df_nodes)):
    d3_nodes.append({
        'name':df_nodes['Label'][i],
        'weight':df_nodes['Weight'][i],
        'id':df_nodes['Id'][i]
    })
    nodes.append(df_nodes['Id'][i])

# edges
df_edges = pd.read_csv('topic/edges_3.csv')
d3_edges = []

for i in range(len(df_edges)):
    source = nodes.index(df_edges['Source'][i])
    target = nodes.index(df_edges['Target'][i])
    weight = df_edges['Weight'][i]
    d3_edges.append({
        'source':source,
        'target':target,
        # 'weight':weight
    })

with open('../../src/data14.json','w') as f:
    json.dump({
        'nodes':d3_nodes,
        'edges':d3_edges
    },f)

print('write over')