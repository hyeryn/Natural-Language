import nltk
import pickle

def sampleData():
    return [
        "Bangalore is the capital of Karnataka.",
        "Steve Jobs was the CEO of Apple.",
        "iPhone was Invented by Apple.",
        "Books can be purchased in Market.",
    ]

def buildDictionary():
    dictionary = {}
    for sent in sampleData():
        partsOfSpeechTags = nltk.pos_tag(nltk.word_tokenize(sent))
        for tag in partsOfSpeechTags:
            value = tag[0]
            pos = tag[1]
            dictionary[value] = pos
    return dictionary

def saveMyTagger(tagger, fileName): #품사 태거에 대한 객체 / 객체 저장 파일 이름
    fileHandle = open(fileName, "wb")
    pickle.dump(tagger, fileHandle) #전체 파일 내용을 저장
    fileHandle.close()

def saveMyTraining(fileName):
    tagger = nltk.UnigramTagger(model=buildDictionary())
    saveMyTagger(tagger, fileName)

def loadMyTagger(fileName):
    return pickle.load(open(fileName, "rb"))

sentence = 'Iphone is purchased by Steve Jobs in Bangalore Market'
fileName = "myTagger.pickle"

saveMyTraining(fileName)

myTagger = loadMyTagger(fileName)

print(myTagger.tag(nltk.word_tokenize(sentence)))