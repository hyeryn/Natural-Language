from nltk.corpus import wordnet as wn
chair = 'chair'

# 워드넷 DB에 저장되어있는 chair 관련 모든 뜻(동의어 집합) 출력
chair_synsets = wn.synsets(chair)
print('의자(Chair)의 뜻 Sysnets :', chair_synsets, '\n\n')

# 해당 리스트의 의미, 정의, 관련 기본형/동의어 + 사용 예시
for synset in chair_synsets:
    print(synset, ': ')
    print('Definition: ', synset.definition())
    print('Lemmas/Synonymous words: ', synset.lemma_names())
    print('Example: ', synset.examples(), '\n')
