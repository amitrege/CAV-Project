import tensorflow as tf
import collections
import sys
import numpy as np

import os
import tarfile

# fix random seed for reproducibility
np.random.seed(7)

Py3 = sys.version_info[0] == 3
print(Py3)

def read_words(filename):
  with tf.gfile.GFile(filename, "r") as f:
    if Py3:
      return f.read().split()
    else:
      return f.read().split()


def build_vocab(filename):
  data = read_words(filename)

  counter = collections.Counter(data)
  
  #count_pairs = sorted(counter.items(), key=lambda x: (-x[1], x[0]))
  #words, k = list(zip(*count_pairs))
  #word_to_id = dict(zip(words, range(1, len(words) + 1)))

  #return word_to_id
  words = list(counter.items())
  most_freq = dict(counter.most_common(50))
  print(most_freq)
  i = 1
  dicts = {}
  for w in words:
    if most_freq.get(w[0],0) == 0:
      dicts[w[0]] = 0
    else:
      dicts[w[0]] = i
      i = i + 1
  return dicts


def file_to_word_ids(filename, word_to_id):
  data = read_words(filename)
  return np.array([word_to_id[word] for word in data if word in word_to_id])