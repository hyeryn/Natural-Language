import nltk

def sampleNE():
    sent = nltk.corpus.treebank.tagged_sents()[0]
    print(nltk.ne_chunk(sent)) #카테고리가 있는 경우는 PERSON/ORGANIZATION 분류됨

def sampleNE2():
    sent = nltk.corpus.treebank.tagged_sents()[0]
    print(nltk.ne_chunk(sent, binary=True))

if __name__ == '__main__':
    sampleNE()
    sampleNE2()