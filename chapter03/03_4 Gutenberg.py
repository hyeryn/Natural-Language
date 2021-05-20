import nltk
from nltk.corpus import gutenberg
print(gutenberg.fileids())

gb_words = gutenberg.words('bible-kjv.txt') #내용전체 복사 -> 길이가 3 이상인 단어
word_filtered = [e for e in gb_words if len(e) >= 3]

stopwords = nltk.corpus.stopwords.words('english') #영어용 불용어 말뭉치 필터링
words = [w for w in word_filtered if w.lower() not in stopwords]

fdist = nltk.FreqDist(gb_words) #일반단어
fdistPlain = nltk.FreqDist(words) #불용어 전처리 텍스트

print('Following are the most common 10 words in the bag')
print(fdist.most_common(10))
print('Following are the most common 10 words in the bag minus the stopwords')
print(fdistPlain.most_common(10))