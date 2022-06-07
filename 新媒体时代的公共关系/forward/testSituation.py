import jieba
import wordcloud

mywordlist = []

def cut():
    stopwords_path = 'stopwords.txt'
    stopwords = [l.replace('\n','') for l in open(stopwords_path,encoding='utf-8')]

    sentence = '#张杰[超话]#传承榜样力量，守护音乐梦想，坚持初心，「益」起前行，助力更多有音乐梦想的孩子[心]'
    seg_list = jieba.lcut(sentence)
    print([l for l in seg_list if l not in stopwords])

from matplotlib import pyplot as plt
from wordcloud import WordCloud

text = '#张杰[超话]#传承榜样力量，守护音乐梦想，坚持初心，「益」起前行，助力更多有音乐梦想的孩子[心]'
ls = jieba.lcut(text)
text = ' '.join(ls)

wc = wordcloud.WordCloud(font_path="msyh.ttc",width=1000,height=700,background_color='white')
wc.generate(text)
plt.imshow(wc)
plt.show()
