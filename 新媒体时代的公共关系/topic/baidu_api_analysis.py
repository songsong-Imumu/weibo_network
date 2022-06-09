from aip import AipNlp
from pprint import pprint
import pandas as pd
import re
App_ID = '26413233'
API_KEY = 'FBOslDGB9sBTaV1awKzMGs8o'
SECRET_KEY = 'FZvaoLrmxB825usGEmIeqmKzUw8Gf7dr'
client = AipNlp(App_ID,API_KEY,SECRET_KEY)

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

df = pd.read_csv('./topic/test.csv')
content = df['content']

scores = []
for i in range(len(content)):
    text = clean(content[i])
    try:
        result = client.sentimentClassify(text)
    except:
        continue
    pprint(result)
