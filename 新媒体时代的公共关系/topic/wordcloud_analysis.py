import jieba
import pandas as pd
import matplotlib.pyplot as plt

stop_words = []
with open('呆萌的停用词表.txt','r',encoding='utf-8') as f:
    for line in f:
        stop_words.append(line.replace('\n',''))

df = pd.read_csv('./topic/人民日报评人教版数学教材配图争议.csv')
content = df['content']
publish_time = df['publish_time']

time_split = ['2022-05-26 00:','2022-05-27 10:','2022-05-27 14:','2022-05-29 00:','2022-05-29 23:']
contents = ''
dict = {}
for i,t in enumerate(publish_time):
    if t >= time_split[0] and t<= time_split[1]:
        con = content[i].replace('人民日报评人教版数学教材配图争议',' ')
        print(con)
        words = jieba.lcut(con)
        for w in words:
            if w in stop_words:
                continue
            else:
                if w in dict:
                    dict[w] += 1
                else:
                    dict[w] = 1

# print(dict)
tuples =  sorted(dict.items(), key=lambda d:d[1], reverse = True)
# print(tuples)

x = []
y = []
for i in range(15):
    x.append(tuples[i][0])
    y.append(tuples[i][1])

print(x)
print(y)



# 词云图
# words = []
# for i in range(len(tuples)):
#     if i == 100 : break
#     words.append(tuples[i][0])
# newtxt = ' '.join(words)
#
# from wordcloud import WordCloud
# print(newtxt)
# wordcloud = WordCloud(font_path='simhei.ttf',background_color='white',
#                       width=1920,height=1080,random_state=0).generate(newtxt)
# plt.imshow(wordcloud,interpolation='bilinear')
# plt.axis('off')
# plt.show()