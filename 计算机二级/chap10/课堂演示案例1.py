from wordcloud import WordCloud
txt='I like Python ,I am learning Python'
wd=WordCloud().generate(txt)
wd.to_file('课堂演示案例1.jpg')
