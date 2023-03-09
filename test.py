
from keras.layers import Input,Activation,Dense
from keras.layers.recurrent import LSTM
from keras.models import Model
from keras.layers.core import RepeatVector,Dropout
from keras.layers.wrappers import TimeDistributed
import numpy as np
def encode(X, seq_len, vocab_size):
    x = np.zeros((len(X), seq_len, vocab_size), dtype=np.float32)
    for ind, batch in enumerate(X):
        for j, elem in enumerate(batch):
            x[ind, j, elem] = 1
    return x


def batch_gen(batch_size=32, seq_len=10, max_no=100):
    step=2000
    while step>0:
        step-=1
        x = np.zeros((batch_size, seq_len, max_no), dtype=np.float32)
        y = np.zeros((batch_size, seq_len, max_no), dtype=np.float32)

        X = np.random.randint(max_no, size=(batch_size, seq_len))
        Y_tmp= np.sort(X, axis=1)
        Y=abs(np.sort(-Y_tmp))

        for ind, batch in enumerate(X):
            for j, elem in enumerate(batch):
                x[ind, j, elem] = 1

        for ind, batch in enumerate(Y):
            for j, elem in enumerate(batch):
                y[ind, j, elem] = 1
        yield x, y

batch_size=64
TIME_STEP=10
INPUT_SIZE=12
CELL_SIZE=15

input=Input(shape=[TIME_STEP,INPUT_SIZE])

x=LSTM(CELL_SIZE,input_shape=(TIME_STEP,INPUT_SIZE))(input)
x=Dropout(0.25)(x)
x=RepeatVector(TIME_STEP)(x)
x=LSTM(CELL_SIZE,return_sequences=True)(x)
x=TimeDistributed(Dense(INPUT_SIZE))(x)
x=Dropout(0.5)(x)
x=Activation('softmax')(x)

model=Model(input,x)

model.summary()
model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])
for ind, (X, Y) in enumerate(batch_gen(batch_size, TIME_STEP, INPUT_SIZE)):
    loss, acc = model.train_on_batch(X, Y)
    if ind % 250 == 0:
        print("ind:",ind)
        testX = np.random.randint(INPUT_SIZE, size=(1, TIME_STEP))
        test = encode(testX, TIME_STEP, INPUT_SIZE)
        print("before is")
        print(testX)
        y = model.predict(test, batch_size=1)
        print("actual sorted output is")
        print(abs(np.sort(-np.sort(testX))))
        print("sorting done by LSTM is")
        print(np.argmax(y, axis=2))
        print("\n")
