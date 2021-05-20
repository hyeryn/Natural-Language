from nltk import PorterStemmer, LancasterStemmer, word_tokenize

raw = "My name is Naximus Decimus Merdius, commander of the Armies of the North," \
      "General ot the Felix Legions and loyal servant to the true emperor," \
      "Marcus Aurelius. Father to a murdered son, husband to a murdered wife." \
      "And I will have my vengeance, in this life or the next."
tokens = word_tokenize(raw)

# 's' 'es' 'e' 'ed' 'al' 로 끝나는 접미사 삭제
porter = PorterStemmer()
pStems = [porter.stem(t) for t in tokens]
print(pStems)

# 'us' 'e' 'th' 'eral' 'ered' 로 끝나는 접미사도 삭제
lancaster = LancasterStemmer()
lStems = [lancaster.stem(t) for t in tokens]
print(lStems)