# ***********************************************************************************************************
# Summary: Creation of the Model and Data preprocessing
#
# Requirements: Python Verison 3.7
#
# Author : Anto
# ***********************************************************************************************************
import tensorflow as tf
import numpy as np
import os
import pickle
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense, LSTM, Dropout
from string import punctuation

# ***********************************************************************************************************
#
# Global Variables
#
# ***********************************************************************************************************

sequence_length = 100
BATCH_SIZE = 128
EPOCHS = 30

# ***********************************************************************************************************
#
#  fill in later
#
# ***********************************************************************************************************


def get_path(path):
    try:
        path = 'Src/scripts.txt'
        basename = os.path.basename(path)
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

def data_stats(text):
    try:
        n_char = len(text)
        unique_char = ''.join(sorted(set(text)))
        no_of_characters = ("No of Characater:", n_char)
        no_of_uniq_characters = ("No Of Unique Characters:", unique_char)
        return no_of_characters, no_of_uniq_characters
    except Exception as e:
        raise Exception(str(e))

test = 'Src/scripts.txt'
a = get_path(test)
b = data_stats(a)
print(b)

# no_of_characters = ("No of Characater:", n_char)
# no_of_uniq_characters = ("No Of Unique Characters:", n_unique_char)


# char2int = {c: i for i, c in enumerate(unique_char)}
# int2char = {i: c for i, c in enumerate(unique_char)}
# pickle.dump(char2int, open(f"{'script'}-char2int.pickle", "wb"))
# pickle.dump(int2char, open(f"{'script'}-int2char.pickle", "wb"))


# encoded_text = np.array([char2int[c] for c in get_path()])
# char_dataset = tf.data.Dataset.from_tensor_slices(encoded_text)
# sequences = char_dataset.batch(
#     2*sequence_length + 1, drop_remainder=True)

# # for sequence in sequences.take(2):
# #     print(''.join([int2char[i] for i in sequence.numpy()]))


# def split_sample(sample):
#     ds = tf.data.Dataset.from_tensors(
#         (sample[:sequence_length], sample[sequence_length]))
#     for i in range(1, (len(sample)-1) // 2):
#         input_ = sample[i: i+sequence_length]
#         target = sample[i+sequence_length]
#         other_ds = tf.data.Dataset.from_tensors((input_, target))
#         ds = ds.concatenate(other_ds)
#     return ds


# dataset = sequences.flat_map(split_sample)


# def one_hot_samples(input_, target):
#     return tf.one_hot(input_, n_unique_char), tf.one_hot(target, n_unique_char)


# dataset = dataset.map(one_hot_samples)

# ds = dataset.repeat().shuffle(1024).batch(BATCH_SIZE, drop_remainder=True)
