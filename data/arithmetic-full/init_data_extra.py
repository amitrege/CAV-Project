import data_gen
import numpy as np
import code_gen 

# Accumulate data and labels in a list
def init_data(dir, data_list, labels_list, known_label):
    fp = code_gen.get_file_paths(dir)
    #max = 0
    for f in fp:
        # Padding vectors to 150 with 0 (250 is arbitrary)
        w_id = data_gen.file_to_word_ids(f, word_to_id)
        w = np.zeros(175)
        w[:w_id.shape[0]] = w_id
        #if max < w_id.shape[0]:
        #    max = w_id.shape[0]
        data_list.append(w)
        labels_list.append(known_label)
    #print(max)
    return data_list, labels_list


# Vectorize data and store
def store_data(data_list, labels_list):
    X = np.vstack(data_list)
    Y = np.array(labels_list)

    np.save('data_extra', X)
    np.save('labels_extra', Y)

# First create concatenations of files of each type
fp = code_gen.get_file_paths('add_correct_extra')
code_gen.concat_files(fp, 'add_correct_extra.txt')

fp = code_gen.get_file_paths('add_wrong_extra')
code_gen.concat_files(fp, 'add_wrong_extra.txt')

# Now, concatenate all concat files to get the vocabulary
code_gen.concat_vocab()

# Build Vocabulary
word_to_id = data_gen.build_vocab('vocab.txt')

# Use lists to avoid overhead of vstack in Numpy
data_list = []
labels_list = []

# For fact1, convert each file into the id format and store in a list
data_list, labels_list = init_data('add_correct_extra', data_list, labels_list, 1)

data_list, labels_list = init_data('add_wrong_extra', data_list, labels_list, 0)

# Store data
store_data(data_list, labels_list)


