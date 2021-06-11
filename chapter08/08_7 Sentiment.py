import nltk
import nltk.sentiment.sentiment_analyzer
import nltk.sentiment.util

def wordBasedSentiment():
    positive_words = ['love', 'hope', 'joy'] #긍정적인 단어 집합 정의
    text = 'Rainfall this year brings lot of hope and joy to Farmers.'.split()
    analysis = nltk.sentiment.util.extract_unigram_feats(text, positive_words)
    print(' -- single word sentiment --')
    print(analysis)

def multiWordBasedSentiment():
    word_sets = [('heavy', 'rains'), ('flood', 'bengaluru')] #단어의 쌍이 존재하는지 여부
    text = 'heavy rains cause flash flooding in bengaluru'.split()
    analysis = nltk.sentiment.util.extract_bigram_feats(text, word_sets)
    print(' -- multi word sentiment --')
    print(analysis)

def markNegativity(): #단어의 부정성 찾기 -> not이후의 단어
    text = 'Rainfall last year did not bring joy to Farmers'.split()
    negation = nltk.sentiment.util.mark_negation(text)
    print(' -- negativity --')
    print(negation)

if __name__ == '__main__':
    wordBasedSentiment()
    multiWordBasedSentiment()
    markNegativity()