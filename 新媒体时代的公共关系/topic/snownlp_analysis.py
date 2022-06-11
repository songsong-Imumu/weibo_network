from snownlp import SnowNLP
import pandas as pd
import re
import jieba
import matplotlib.pyplot as plt
def clean(text):
    text = re.sub(r"(回复)?(//)?\s*@\S*?\s*(:| |$)", " ", text)  # 去除正文中的@和回复/转发中的用户名
    text = re.sub(r"\[\S+\]", "", text)      # 去除表情符号
    # text = re.sub(r"#\S+#", "", text)      # 保留话题内容
    URL_REGEX = re.compile(
        r'(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?«»“”‘’]))',
        re.IGNORECASE)
    text = re.sub(URL_REGEX, "", text)       # 去除网址
    text = text.replace("转发微博", "")       # 去除无意义的词语
    text = re.sub(r"\s+", " ", text) # 合并正文中过多的空格
    return text.strip()

def filter_html(text):
    # text为包含html标签内容
    content = re.sub("<[^>]*?>", "", text)
    return content

averages = []
def sentiment_score(input_file, text_col = 'content'):
    df = pd.read_csv(input_file)
    sentiment_score_col = 'sentiment_score'
    is_scored_col = 'has_scored'
    df[is_scored_col] = [False for _ in range(df.shape[0])]
    for index, row in df.iterrows():
        # print(f'{index + 1}/{df.shape[0]}')
        if row[is_scored_col] == True:
            continue
        text = row[text_col]
        # 去除 html 标签
        text = filter_html(text)
        text = clean(text)
        text = jieba.lcut(text)
        if len(text) == 0 or text == None:
            # 本行没有文本
            sentiment = -1
        else:
            sum = 0
            for t in text:
                sentiment = SnowNLP(t).sentiments
                sum += sentiment
                # if sentiment > max :
                #     max = sentiment
            average = sum / len(text)
        averages.append(average)
            # sentiment = SnowNLP(text).sentiments
        df.loc[index, sentiment_score_col] = average
        df.loc[index, is_scored_col] = True

    df.to_csv(input_file, index=False, encoding='utf-8-sig')

# sentiment_score('./topic/test.csv')
# print(averages)

df = pd.read_csv('./topic/人民日报评人教版数学教材配图争议.csv')
# content = df['content']
# print(list(content))
score = list(df['sentiment_score'])
count1 = 0
count0 = 0
count11 = 0
for s in score:
    if s >= 0.6:
        count1 += 1
    elif s >= 0.55:
        count0 += 1
    else:
        count11 += 1
print(len(score))
print(count1)
print(count0)
print(count11)
# print(score)
# print(len(score))
# plt.plot(range(len(score)),score)
# plt.show()
