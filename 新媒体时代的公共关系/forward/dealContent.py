import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import json
import jieba
from wordcloud import WordCloud,STOPWORDS

class createContent():
    def __init__(self,path,index):
        self.path = path
        self.index = index

    # 读csv to dataframe
    def readFile(self):
        df = pd.read_csv(self.path)
        self.content = df['content']
        self.content = list(self.content)

    def get_cut_sentence(self):
        content = self.content
        sentences = [cut(s) for s in content]
        self.sentences = sentences

    def create_dictionary(self):
        words = {}
        for sentence in self.sentences:
            for word in sentence:
                if word not in words :
                    words[word] = 1
                else :
                    words[word] += 1
        print(words)
        words = [{'name':w,'value':words[w]} for w in words]
        print(words)
        print([w['name'] for w in words])
        self.words = words

    def draw_word_cloud(self):
        wc = WordCloud(
            font_path=r'STKAITI.TTF',
            background_color='white',
            stopwords=STOPWORDS
        )
        wc.generate(self.words)
        plt.figure("WordCloud_test1")
        # 以图片的形式显示词云
        plt.imshow(wc)
        # 关闭图像坐标系
        plt.axis("off")
        plt.show()

def cut(sentence):
    stopwords_path = './stopwords.txt'
    stopwords = [l.replace('\n', '') for l in open(stopwords_path, encoding='utf-8')]

    # sentence = '#张杰[超话]#传承榜样力量，守护音乐梦想，坚持初心，「益」起前行，助力更多有音乐梦想的孩子[心]'
    seg_list = jieba.lcut(sentence)
    return [l for l in seg_list if l not in stopwords]

if __name__ == '__main__':

    # path = './forward/4755716352511591.csv'
    path = './forward/4756658112430923.csv'
    index = 8

    assignment = createContent(path,index)
    assignment.readFile()
    assignment.get_cut_sentence()
    assignment.create_dictionary()
    # assignment.draw_word_cloud()