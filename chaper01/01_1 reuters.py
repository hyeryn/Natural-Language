# nltk 설치 완료
# import nltk
# nltk.download()

# nltk에서 reuters 코퍼스 엑세스
from nltk.corpus import reuters

# 말뭉치에서 무엇을 쓸 수 있는지 확인
files = reuters.fileids()
print(files)

# 파일의 실제 내용에 접근
words16097 = reuters.words(['test/16097'])
print(words16097) #test/16097내의 단어목록을 표시
word20 = reuters.words(['test/16097'])[:20] #20개의 단어만 엑세스
print(word20)

# 계층적 분류 중 카테고리 목록 출력
reutersGenre = reuters.categories() #90개의 범주
print(reutersGenre)

# 항목에 엑세스 -> 행마다 하나의 완전한 문장으로 출력
for w in reuters.words(categories=['bop','cocoa']): #두 카테고리 선택 후
    print(w+' ',end='') #해당 파일의 모든 내용 출력
    if(w is '.'): #마침표가 나올때마다 새로운 행 삽입
        print()
