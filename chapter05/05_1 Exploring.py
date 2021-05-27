import nltk
simpleSentence = "Bangalore is the capital of Karnataka."
wordsInSentence = nltk.word_tokenize(simpleSentence)
print(wordsInSentence)
partsOfSpeechTags = nltk.pos_tag(wordsInSentence) #품사의 식별 가능
print(partsOfSpeechTags)
