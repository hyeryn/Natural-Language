from nltk import word_tokenize, PorterStemmer, WordNetLemmatizer

raw = "My name is Naximus Decimus Merdius, commander of the Armies of the North," \
      "General ot the Felix Legions and loyal servant to the true emperor," \
      "Marcus Aurelius. Father to a murdered son, husband to a murdered wife." \
      "And I will have my vengeance, in this life or the next."
tokens = word_tokenize(raw)

porter = PorterStemmer()
pStems = [porter.stem(t) for t in tokens]
print(pStems)

#스테머보다 기본형을 얻는데 뛰어남 (명사를 cut하지 않음)
lemmatizer = WordNetLemmatizer()
lemmas = [lemmatizer.lemmatize(t) for t in tokens]
print(lemmas)