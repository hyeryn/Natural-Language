import nltk
from nltk.corpus import brown

# brown의 장르 확인
print(brown.categories())

# 장르 선택 후 장르의 텍스트에서 뽑아내고자하는 whwords 선택
genres = ['fiction', 'humor', 'romance']
whwords = ['what', 'which', 'how', 'why', 'when', 'where', 'who']

# 장르 리스트에서 whwords count
for i in range(0, len(genres)):
    genre = genres[i]
    print()
    print("'"+genre+"'wh 단어 분석'")
    genre_text = brown.words(categories=genre)

    # FreqDist() 단어 목록을 받아들이고 해당 빈도를 반환
    fdlist = nltk.FreqDist(genre_text)

    for wh in whwords:
        print(wh + ":", fdlist[wh], end=' ') #해당 index의 단어 개수를 출력
