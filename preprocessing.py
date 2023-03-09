import json
from collections import Counter
from keras.utils import to_categorical
import numpy as np
def get_data(filename):
    with open(filename) as f:
        list=json.load(f)
    return list
def counter(note):
    counters=Counter(note)
    note_count=sorted(counters.items(),key=lambda x:-x[1])
    notes,_=zip(*note_count)
    note_to_id={note:id for id,note in enumerate(notes)}
    return note_to_id
note=get_data('origin.json')
fin=counter(note)
X_train=[]
Y_train=[]
sequence_batch=100
for i in range(len(note)-sequence_batch):
    X_pre=note[i:i+sequence_batch]
    Y_pre=note[i+sequence_batch]
    X_train.append([fin[note]for note in X_pre])
    Y_train.append(fin[Y_pre])
X_train=X_train[:30000]
Y_train=Y_train[:30000]
X_one_hot = to_categorical(X_train)
Y_one_hot = to_categorical(Y_train)
