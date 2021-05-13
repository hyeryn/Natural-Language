from nltk.corpus import wordnet as wn
woman = wn.synset('woman.n.01')
bed = wn.synset('bed.n.01')

print(woman.hypernyms()) #동일한 직계부모 노드의 동의어 집합 반환 -> woman : 성인&여성의 범주에 속함
woman_paths = woman.hypernym_paths() #집합의 리스트를 반환

# 루트 노드에서 woman 노드로 경로를 출력
for idx, path in enumerate(woman_paths):
    print('\n\n상위어 경로 : ', idx + 1)
    for synset in path:
        print(synset.name(), ', ', end='')