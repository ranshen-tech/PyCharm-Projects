"""
jieba库：将一段中文文本分割成中文词语的序列
"""
# import jieba
# print(jieba.lcut('全国计算机等级考试python科目'))  # 将字符串分隔为等量的中文词组，返回列表类型
# jieba.add_word('python科目')  # 向jieba词库增加新的词组
# print(jieba.lcut('全国计算机等级考试python科目'))
# print(jieba.lcut('全国计算机等级考试Python科目'))


"""
wordcloud库：根据文本产生词云,默认空格或标点分隔符对目标文本进行分词处理。
对于中文文本，一般先将文本分词处理，然后以空格拼接，然后调用wordcloud库函数
"""
# from wordcloud import WordCloud  # 从库中导入其中一个类
# txt = 'I like Python, I am learning Python.'
# f = WordCloud().generate(txt)
# f.to_file('wordcloud.jpg')  # 这个挺关键


import jieba
from wordcloud import WordCloud
txt = '程序设计语言是计算机能够理解和识别用户操作意图的一种交互体系，它按照特定规则组织、执行计算机指令，使计算机能够自动进行各种运算处理'
words = jieba.lcut(txt)
new_txt = ' '.join(words)
print(new_txt)
wordcloud = WordCloud(font_path='System/Library/fonts/PingFang.ttc').generate(new_txt)
wordcloud.to_file('wordcloud2.jpg')
