__author__ = 'ranshen0519@icloud.com'

"""
初始难度分为 0，每当出现一次生词就将难度分 +5，最终的难度分就代表这篇文章的难度。
提示：
统计生词数的同时进行难度分的计算，因此可以合并成一个get_difficulty()函数
参数为每个单词出现次数的字典和生词列表。初始难度分为 0，遍历生词列表，如果生词在单词出现次数的字典中，
难度分增加 5 * 该单词出现的次数，最终即可得到难度分。
"""

article = '''This is a photograph of our village.
Our village is in a valley.
It is between two hills.
The village is on a river.
Here is another photograph of the village.
My wife and I are walking along the banks of the river.
We are on the left.
There is a boy in the water.
He is swimming across the river.
Here is another photograph.
This is the school building.
It is beside a park.
The park is on the right.
Some children are coming out of the building.
Some of them are going into the park.
'''

new_words = [
    'photograph',
    'village',
    'valley',
    'between',
    'hills',
    'another',
    'prep',
    'wife',
    'along',
    'banks',
    'water',
    'swimming',
    'building',
    'park',
    'into'
]


def get_word_count(articles):
    word_count = {}
    word_list = articles.lower().replace('.', '').split()
    for word in word_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count


def get_difficulty(word_counts, new_word, level=0):
    for word in new_word:
        if word in word_counts:
            level += 5 * word_counts[word]
    return level


word_num = get_word_count(article)
difficulty = get_difficulty(word_num, new_words)
print(difficulty)
