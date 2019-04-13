import numpy as np
import collections
import sys

import os
import tarfile

import glob

# For getting data for colab from drive
def extract_tar(filename):
  t = tarfile.open(filename)
  t.extractall()

# Assuming the dir is the working dir
def get_file_paths(dirname):
  files = os.listdir('./' + dirname)
  #Y = np.full(len(files), known_label, dtype = int)
  
  file_paths = ['./' + dirname + '/' + f for f in files]
  
  return file_paths
  
def concat_files(file_paths, output_file):
  # Makes it easier to concat all files later
  output_file = "concat-" + output_file
  
  with open('./concat/' + output_file, 'w') as outfile:
    for fname in file_paths:
        with open(fname) as infile:
            outfile.write(infile.read())

def concat_vocab():
    read_files = glob.glob("./concat/*.txt")

    with open("vocab.txt", "wb") as outfile:
        for f in read_files:
            with open(f, "rb") as infile:
                outfile.write(infile.read())

# For use in CoLab  
# extract_tar('code.tar')