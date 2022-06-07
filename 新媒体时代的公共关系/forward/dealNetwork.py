import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import json

class createNetwork():
    def __init__(self,path,index):
        self.path = path
        self.index = index

    # 读csv to dataframe
    def readFile(self):
        df = pd.read_csv(self.path)
        self.content = df['content']
        self.user_name = df['user_name']

    # 从转发关系中提取网络关系
    def get_nodes_edges(self,root):
        content = self.content
        user_name = self.user_name

        # 构建点
        nodes = {root: 0}
        count = 1
        for name in user_name:
            if name not in nodes:
                nodes[name] = count
                count += 1

        # 构建连边
        edges = []
        for i, sth in enumerate(content):
            # 一度邻居
            if '@' not in sth:
                edges.append({
                    'source': 0,
                    'target': nodes[user_name[i]]
                })

            if '@' in sth:
                # 获得链，转发用户名称
                nameArray = fromContentgetNames(sth)
                for j, name in enumerate(nameArray):
                    if name not in nodes: continue
                    if nameArray[j - 1] not in nodes: continue
                    if j == 0:
                        continue
                    else:
                        edges.append({
                            'source': nodes[nameArray[j]],
                            'target': nodes[nameArray[j - 1]]
                        })
                # 连接最后一条边
                if len(nameArray) == 0: continue
                if nameArray[len(nameArray) - 1] not in nodes: continue
                value = {
                    'source': nodes[nameArray[len(nameArray) - 1]],
                    'target': nodes[user_name[i]]
                }
                edges.append(value)

        # 修改nodes的数据结构
        newnodes = []
        for sth in nodes:
            newnodes.append({
                'name': sth
            })
        self.nodes = newnodes
        self.edges = edges

    # 去除离群点
    def remove(self):
        nodes = self.nodes
        edges = self.edges
        # 构建networkx图
        G = nx.Graph()
        G.add_nodes_from([i for i,_ in  enumerate(nodes)])
        G.add_edges_from([(e['source'],e['target']) for e in edges])
        # 最大连通图
        largest = max(nx.connected_components(G),key=len)
        largest_connected_subgraph = G.subgraph(largest)

        # 重新转换为json,注意nodes和edges的下标
        newNodes = []
        for index,node in enumerate(nodes):
            if index not in largest_connected_subgraph.nodes():
                newNodes.append({'name':''})
            else :
                newNodes.append(node)
        edges = [{
            'source':e[0],
            'target':e[1]
        } for e in largest_connected_subgraph.edges()]

        self.nodes = newNodes
        self.edges = edges

    # 写文件
    def down_to_json(self):
        with open('./data'+str(index)+'.json','w') as f:
            json.dump({
                'nodes':self.nodes,
                'edges':self.edges
            },f)

# 从评论说获取用户名称
def fromContentgetNames(string):
    start = 0
    end = 0
    startflag = 0
    endflag = 0
    array = []
    for i,sth in enumerate(string):
        if sth == '@':
            startflag = 1
            start = i
        if sth == ':':
            endflag = 1
            end = i
        if startflag == 1 and endflag == 1:
            startflag = 0
            endflag = 0
            array.append(string[start+1:end])
    return array

if __name__ == '__main__':
    # 微博 id.csv
    # path = './forward/4740001465896702.csv'
    # path = './4740396926371179.csv'
    # 张文宏 3
    # path = './forward/4750364861792281.csv'
    # 杭州碎尸案二审 4
    # path = './forward/4755988341588168.csv'
    # 老坛酸菜牛肉面 5
    # path = './forward/4747401099480956.csv';
    # 教授 6
    # path = './forward/4755587935769216.csv'
    # 新浪公益 7
    # path = './forward/4755716352511591.csv'
    # 昆明专升本
    # path = './forward/4756658112430923.csv'
    # 人教版教材
    # path = './forward/4773311474829092.csv'
    # index = 11
    # 地瓜熊老六，人教版教材
    path = './forward/4773283217541757.csv'
    index = 12

    assignment = createNetwork(path,index)
    assignment.readFile()
    assignment.get_nodes_edges('地瓜熊老六')
    assignment.remove()
    assignment.down_to_json()
