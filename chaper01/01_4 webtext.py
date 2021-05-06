import nltk, matplotlib
from nltk.corpus import webtext
print(webtext.fileids())

# 목표 데이터가 들어있는 txt파일을 담고 빈도 분포를 실행
fileid = 'singles.txt'
wbt_words = webtext.words(fileid)
fdlist = nltk.FreqDist(wbt_words)

# 데이터 빈도수 이용
print("최대 발생 토큰 '", fdlist.max(), "'수: ", fdlist[fdlist.max()])
print('말뭉치 내 고유 토큰 수 : ', fdlist.N())
print('개인 광고의 빈도 분포')
print(fdlist.tabulate()) #전체 빈도를 표로 나타냄
fdlist.plot(cumulative=True) #누적빈도의 도수분포그래프
