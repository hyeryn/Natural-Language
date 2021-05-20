# 임의로 두 개의 객체 생성
namesList = ['혜린', '헤링', '강아지', '고양이']
sentence = '자유롭게 여행다니면서 맛있는거 먹는 인생이 제일 좋다'

# join
names = '; '.join(namesList)
print(type(names), ":", names)

# split
wordList = sentence.split(' ')
print(type(wordList), ":", wordList)

# 산술연산
additionExample = '파이썬'+'파이썬'
multiplicationExample = '파이썬' * 3
print(additionExample, " / ", multiplicationExample)

# 문자열 인덱스
str = 'Python NLTK'
print(str[1], " / ", str[-3])