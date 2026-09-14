import jieba

sentence = "我爱自然语言处理"
words = jieba.cut(sentence)
print("/".join(words))
