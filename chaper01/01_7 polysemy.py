#워드넷으로 명사, 동사, 형용사, 부사의 다의어 평균 계산

from nltk.corpus import wordnet as wn
type = 'n' # 품사의 유형을 명사로 설정(n-명사, v-동사, r-부사, a-형용사)

synsets = wn.all_synsets(type) # 존재하는 명사 유형 n의 모든 synset 반환

# lemma 리스트로 통합
lemmas = []
for synset in synsets:
    for lemma in synset.lemmas():
        lemmas.append(lemma.name())

# 중복을 제거하고 개별 lemmas count
lemmas = set(lemmas) #리스트를 집합으로 변환하면 중복제거

count = 0
for lemma in lemmas:
    count = count + len(wn.synsets(lemma, type))

print('개별 기본형 합계: ', len(lemmas))
print('총 뜻: ', count)
print(type, '(명사)의 다의어 평균: ', count/len(lemmas))