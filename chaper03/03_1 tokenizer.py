from nltk.tokenize import LineTokenizer, SpaceTokenizer, TweetTokenizer
from nltk import word_tokenize

lTokenizer = LineTokenizer() #입력 문자열을 줄 단위로 분류
print("Line tokenizer 출력 : ", lTokenizer.tokenize("My name is HyeRyn Park"
                                                  "im from Korea. \nHi everyone"
                                                  "\n nice to meet you"))

rawText = "By 11 o'clock on Sunday, the doctor shall open the dispensary."
sTokenizer = SpaceTokenizer() #공백문자 기준으로 분류
print("Space tokenizer 출력 : ", sTokenizer.tokenize(rawText))

print("Word tokenizer 출력 : ", word_tokenize(rawText)) #단어 구두점도 분류

tTokenizer = TweetTokenizer() #특수 문자열을 기준으로 분류
print('Tweet tokenizer 출력 : ', tTokenizer.tokenize("This is a coool "
                                                   "#dummysmiley: :-) :-P <3"))