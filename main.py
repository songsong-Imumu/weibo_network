import pandas as pd
import json
df = pd.read_csv("./data.csv")
nodes = {}
count = 0
for i in range(len(df)):
  source = df['source'][i].replace('name=','')
  target = df['target'][i].replace('name=','')
  if source not in nodes:
    nodes[source] = count
    count += 1
  if target not in nodes:
    nodes[target] = count
    count += 1

edges = []
for i in range(len(df)):
  source = df['source'][i].replace('name=','')
  target = df['target'][i].replace('name=','')
  edges.append({
    'source':nodes[source],
    'target':nodes[target],
  })
# print(nodes)
# print(edges)
newnodes = []
for sth in nodes:
  newnodes.append({
    'name':sth
  })
with open("./data.json",'w') as f:
  json.dump({
    'nodes':newnodes,
    'edges':edges,
  },f)
    