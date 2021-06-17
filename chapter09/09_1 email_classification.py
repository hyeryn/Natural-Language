from sklearn.datasets import fetch_20newsgroups

newsgroups_train = fetch_20newsgroups(subset='train')
newsgroups_test = fetch_20newsgroups(subset='test')

x_train = newsgroups_train.data
x_test = newsgroups_test.data

y_train = newsgroups_train.target
y_test = newsgroups_test.target

print("List of all 20 categories:")
print(newsgroups_train.target_names)
print("\n")
print("Sample Email:")
print(x_train[0])
print("Sample Target Category:")
print(y_train[0])
print(newsgroups_train.target_names[y_train[0]])

# Used for pre-processing data
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import string
import pandas as pd
from nltk import pos_tag
from nltk.stem import PorterStemmer


def preprocessing(text):
    #단어분할 -> 문장부호제거
    text2 = " ".join("".join([" " if ch in string.punctuation else ch for ch in text]).split())
    #토큰화
    tokens = [word for sent in nltk.sent_tokenize(text2) for word in
              nltk.word_tokenize(sent)]
    #소문자로 변환(말뭉치 중복 줄이기)
    tokens = [word.lower() for word in tokens]
    #불용어처리
    stopwds = stopwords.words('english')
    tokens = [token for token in tokens if token not in stopwds]
    #최소 3단어 이상의 길이유지(의미없는 단어의 제거)
    tokens = [word for word in tokens if len(word) >= 3]
    #스테밍(접미사 처리->어간추출)
    stemmer = PorterStemmer()
    try:
        tokens = [stemmer.stem(word) for word in tokens]

    except:
        tokens = tokens
    #원형복원->어근으로 줄어듦
    tagged_corpus = pos_tag(tokens)
    #품사변환
    Noun_tags = ['NN', 'NNP', 'NNPS', 'NNS']
    Verb_tags = ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']

    lemmatizer = WordNetLemmatizer()
    #각 카테고리에 맞는 품사 적용
    def prat_lemmatize(token, tag):
        if tag in Noun_tags:
            return lemmatizer.lemmatize(token, 'n')
        elif tag in Verb_tags:
            return lemmatizer.lemmatize(token, 'v')
        else:
            return lemmatizer.lemmatize(token, 'n')
    #토큰화 후 재결합 -> 문자열 형태로
    pre_proc_text = " ".join([prat_lemmatize(token, tag) for token, tag in tagged_corpus])

    return pre_proc_text

#학습 데이터에 대해 전처리 적용
x_train_preprocessed = []
for i in x_train:
    x_train_preprocessed.append(preprocessing(i))

x_test_preprocessed = []
for i in x_test:
    x_test_preprocessed.append(preprocessing(i))

# building TFIDF vectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer(min_df=2, ngram_range=(1, 2), stop_words='english',
                             max_features=10000, strip_accents='unicode', norm='l2')

x_train_2 = vectorizer.fit_transform(x_train_preprocessed).todense()
x_test_2 = vectorizer.transform(x_test_preprocessed).todense()

# Deep Learning modules -> 전처리 완료한 TF-IDF 벡터는 딥러닝코드로 넘겨
import numpy as np
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.optimizers import Adadelta, Adam, RMSprop
from keras.utils import np_utils

# Definiting hyper parameters
np.random.seed(1337)
nb_classes = 20 #클래스수 20
batch_size = 64 #배치(일괄처리)사이즈 64
nb_epochs = 20 #에포크 20

Y_train = np_utils.to_categorical(y_train, nb_classes) #20개 카테고리 -> 원핫인코딩벡터로 변환

# Deep Layer Model building in Keras
# del model
# 3개의 레이어(각각은 1000,500,50개의 뉴런 + 아담 옵티마이저 + 각 레이어 드롭아웃은 50%)

model = Sequential()

model.add(Dense(1000, input_shape=(10000,)))
model.add(Activation('relu'))
model.add(Dropout(0.5))

model.add(Dense(500))
model.add(Activation('relu'))
model.add(Dropout(0.5))

model.add(Dense(50))
model.add(Activation('relu'))
model.add(Dropout(0.5))

model.add(Dense(nb_classes))
model.add(Activation('softmax'))

model.compile(loss='categorical_crossentropy', optimizer='adam')

print(model.summary()) #10000 시작점에서 각 3개의 뉴런층이 주어진 이메일을 20개의 범주 중 하나로 분류

# Model Training
model.fit(x_train_2, Y_train, batch_size=batch_size, epochs=nb_epochs, verbose=1)

# Model Prediction
y_train_predclass = model.predict_classes(x_train_2, batch_size=batch_size)
y_test_predclass = model.predict_classes(x_test_2, batch_size=batch_size)

from sklearn.metrics import accuracy_score, classification_report

print("\n\nDeep Neural Network  - Train accuracy:"), (round(accuracy_score(y_train, y_train_predclass), 3)) #학습 데이터셋 정확도
print("\nDeep Neural Network  - Test accuracy:"), (round(accuracy_score(y_test, y_test_predclass), 3)) #테스트 데이터셋 정확도

print("\nDeep Neural Network  - Train Classification Report")
print(classification_report(y_train, y_train_predclass))

print("\nDeep Neural Network  - Test Classification Report")
print(classification_report(y_test, y_test_predclass))