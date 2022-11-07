# ***********************************************************************************************************
# Summary: Creation of the Model and Data preprocessing
#
# Requirements: Python Verison 3.7
#
# Author : Anto
# ***********************************************************************************************************
from keras.models import Sequential
from keras.layers import Dense, Dropout, LSTM
from keras.optimizers import RMSprop
import numpy as np
import random
import sys


# ***********************************************************************************************************
#
# Global Variables
#
# ***********************************************************************************************************

# ***********************************************************************************************************
#
#  fill in later
#
# ***********************************************************************************************************

def get_path():
    try:
        path = 'Src/scripts.txt'
        text = open(path, encoding="utf-8").read()
        text = text.lower()
        return text
    except Exception as e:
        raise Exception(str(e))




# ***********************************************************************************************************
#
#  fill in later
#
# ***********************************************************************************************************

file = get_path()

chars = sorted(list(set(file)))

char_to_int = dict((c,i) for i,c in enumerate(chars))

int_to_char = dict((i,c) for i,c in enumerate(chars))

n_chars = len(file)
n_vocab = len(chars)

seq_length = 60  
step = 10   
sentences = []   
next_chars = []  
for i in range(0, n_chars - seq_length, step):  
    sentences.append(file[i: i + seq_length])  
    next_chars.append(file[i + seq_length])  
n_patterns = len(sentences)    


x = np.zeros((len(sentences), seq_length, n_vocab), dtype=np.bool_)
y = np.zeros((len(sentences), n_vocab), dtype=np.bool_)
for i, sentence in enumerate(sentences):
    for t, char in enumerate(sentence):
        x[i, t, char_to_int[char]] = 1
    y[i, char_to_int[next_chars[i]]] = 1

model = Sequential()
model.add(LSTM(128, input_shape=(seq_length, n_vocab)))
model.add(Dense(n_vocab, activation='softmax'))

optimizer = RMSprop(lr=0.01)
model.compile(loss='categorical_crossentropy', optimizer=optimizer)
model.summary()

from keras.callbacks import ModelCheckpoint

filepath="saved_weights/saved_weights-{epoch:02d}-{loss:.4f}.hdf5"
checkpoint = ModelCheckpoint(filepath, monitor='loss', verbose=1, save_best_only=True, mode='min')

callbacks_list = [checkpoint]




history = model.fit(x, y,
          batch_size=128,
          epochs=50,   
          callbacks=callbacks_list)

model.save('my_saved_weights_jungle_book_50epochs.h5')