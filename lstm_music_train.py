import json
from keras.utils import to_categorical

from preprocessing import Y_train
# X_train=[]
Y_train=[]
# file=open ('preprocessed_train_data/X_train.json','r')
# for line in file.readlines():
#     dic=json.loads(line)
#     X_train.append(dic)
file_y=open ('preprocessed_train_data/Y_train.json','r')
for line in file_y.readlines():
    dic=json.loads(line)
    Y_train.append(dic)
# X_one_hot = to_categorical(X_train)
Y_one_hot = to_categorical(Y_train)
# print("X_one_hot shape is:",X_one_hot.shape)
print("Y_one_hot shape is:",Y_one_hot.shape)