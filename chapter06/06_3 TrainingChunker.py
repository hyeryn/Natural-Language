import nltk
from nltk.corpus import conll2000
from nltk.corpus import treebank_chunk

def mySimpleChunker():
    grammer = 'NP: {<NNP>+}'
    return nltk.RegexpParser(grammer)

def test_nothing(data):
    cp = nltk.RegexpParser("")
    print(cp.evaluate(data))

def test_mysimplechunker(data):
    schunker = mySimpleChunker()
    print(schunker.evaluate(data))

datasets = [
    conll2000.chunked_sents('test.txt', chunk_types=['NP']),
    treebank_chunk.chunked_sents()
]

for dataset in datasets:
    test_nothing(dataset[:50])
    test_mysimplechunker(dataset[:50])