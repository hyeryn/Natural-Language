import nltk

def understandWordSenseExamples():
    words = ['wind', 'date', 'left']
    print("-- examples --")
    for word in words:
        syns = nltk.corpus.wordnet.synsets(word) #동의어 집합 가져와서 현재의 집합을 변수에 저장
        for syn in syns[:2]:
            for example in syn.examples()[:2]:
                print("{} -> {} -> {}".format(word, syn.name(), example))


def understandBuiltinWSD():
    print("-- built-in wsd --")
    maps = [ # 분석할 문장 / 의미를 찾고자 하는 단어 / 단어의 품사
        ('Is it the fish net that you are using to catch fish ?', 'fish', 'n'),
        ('Please dont point your finger at others.', 'point', 'n'),
        ('I went to the river bank to see the sun rise', 'bank', 'n'),
    ]
    for m in maps:
        print("Sense '{}' for '{}' -> '{}'".format(m[0], m[1], nltk.wsd.lesk(m[0], m[1], m[2])))

if __name__ == '__main__':
    understandWordSenseExamples()
    understandBuiltinWSD()