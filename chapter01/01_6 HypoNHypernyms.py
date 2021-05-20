from nltk.corpus import wordnet as wn
woman = wn.synset('woman.n.01')
bed = wn.synset('bed.n.01')

# A - 상위어 작업: 두 개의 상위어가 존재하지만 / entity에서 woman까지 네 경로 존재
print(woman.hypernyms()) #동일한 직계부모 노드의 동의어 집합 반환 -> woman : 성인&여성의 범주에 속함
woman_paths = woman.hypernym_paths() #집합의 리스트를 반환

# 루트 노드에서 woman 노드로 경로를 출력
for idx, path in enumerate(woman_paths):
    print('\n\n상위어 경로 : ', idx + 1)
    for synset in path:
        print(synset.name(), ', ', end='')
        
# B - 하위어 작업: 20개의 하위어 존재
type_of_beds = bed.hyponyms()
print('\n\nbed의 형태(하위어) : ', type_of_beds)

# 쉬운 예시 -> bed의 하위어 표시(간편한 중첩문)
print(sorted(set(lemma.name() for synset in type_of_beds for lemma in synset.lemmas())))

