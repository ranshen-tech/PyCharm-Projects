from wordcloud import WordCloud
txt='I like Python,I am learning python'
wordcloud=WordCloud().generate(txt)
wordcloud.to_file('test.jpg')

