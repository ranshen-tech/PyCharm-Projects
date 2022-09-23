import jieba
from wordcloud import WordCloud
from scipy.misc import imread
f=open('保利地产：2018年年度报告.txt','r',encoding='utf-8')
txt=f.read()
txt=' '.join(jieba.lcut(txt))
mask=imread('picture.png')
wordcloud=WordCloud(background_color='white',\
                    width=800,\
                    height=600,\
                    max_words=100,\
                    max_font_size=80,\
                    font_path='msyh.ttc',\
                   
                    mask=mask).generate(txt)
wordcloud.to_file('报告.jpg')


