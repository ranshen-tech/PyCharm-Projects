import jieba
from wordcloud import WordCloud
txt='程序设计语言是计算机能够理解和识别用户操作意图的一种交互体系，它按照特定规则组织、计算机指令，使用计算机能够自动进行各种运算处理'
words=jieba.lcut(txt)
newtxt=' '.join(words)
wordcloud=WordCloud(font_path='msyh.ttc').generate(newtxt)
wordcloud.to_file('词云中文案例.png')
