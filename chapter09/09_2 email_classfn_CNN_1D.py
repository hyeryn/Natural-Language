from __future__ import print_function

import pandas as pd

from keras.preprocessing import sequence
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.layers import Embedding
from keras.layers import Conv1D, GlobalMaxPooling1D
from keras.datasets import imdb #일련의 감정 데이터셋

from sklearn.metrics import accuracy_score,classification_report


# set parameters: -> 최대피처/추출할단어수 6000, 개별문장최대길이 400
max_features = 6000
max_length = 400
(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=max_features)
print(len(x_train), 'train observations') #학습된 모델과 테스트할 모델의 관측치 수
print(len(x_test), 'test observations')


# Creating numbers to word mapping -> 해당 단어와 해당 정수 인덱스 값의 딕셔너리 매핑
wind = imdb.get_word_index()
revind = dict((v,k) for k,v in wind.iteritems())
#영어 단어가 아닌 숫자로 결과가 보여짐
print (x_train[0])
print (y_train[0])

#디코딩: 역매핑딕셔너리
def decode(sent_list):
    new_words = []
    for i in sent_list:
        new_words.append(revind[i])
    comb_words = " ".join(new_words)
    return comb_words
#숫자 매핑을 텍스트로 변환 후 출력
print (decode(x_train[0]))


# 효율적 연산을 위한 패드 배열 : 모든 관측치를 하나의 고정된 차원으로 가져와 속도를 향상시키고 계산을 가능하게 끔 만듦
#-> 최대 길이기 400단인 추가 문장을 더하기 위해서
x_train = sequence.pad_sequences(x_train, maxlen=max_length)
x_test = sequence.pad_sequences(x_test, maxlen=max_length)
print('x_train shape:', x_train.shape)
print('x_test shape:', x_test.shape)


# Deep Learning architecture parameters
batch_size = 32
embedding_dims = 60
num_kernels = 260
kernel_size = 3
hidden_dims = 300
epochs = 3


# Building the model
model = Sequential()

model.add(Embedding(max_features,embedding_dims,input_length=max_length))
model.add(Dropout(0.2))

model.add(Conv1D(num_kernels,kernel_size,padding='valid',activation='relu',strides=1))
model.add(GlobalMaxPooling1D())

model.add(Dense(hidden_dims))
model.add(Dropout(0.5))
model.add(Activation('relu'))

model.add(Dense(1))
model.add(Activation('sigmoid'))

model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])

print (model.summary())

model.fit(x_train, y_train,batch_size=batch_size,epochs=epochs,validation_split=0.2)


#Model Prediction
y_train_predclass = model.predict_classes(x_train,batch_size=batch_size)
y_test_predclass = model.predict_classes(x_test,batch_size=batch_size)

y_train_predclass.shape = y_train.shape
y_test_predclass.shape = y_test.shape


# Model accuracies & metrics calculation
print (("\n\nCNN 1D  - Train accuracy:"),(round(accuracy_score(y_train,y_train_predclass),3)))
print ("\nCNN 1D of Training data\n",classification_report(y_train, y_train_predclass))
print ("\nCNN 1D - Train Confusion Matrix\n\n",pd.crosstab(y_train, y_train_predclass,rownames = ["Actuall"],colnames = ["Predicted"]))

print (("\nCNN 1D  - Test accuracy:"),(round(accuracy_score(y_test,y_test_predclass),3)))
print ("\nCNN 1D of Test data\n",classification_report(y_test, y_test_predclass))
print ("\nCNN 1D - Test Confusion Matrix\n\n",pd.crosstab(y_test, y_test_predclass,rownames = ["Actuall"],colnames = ["Predicted"]))