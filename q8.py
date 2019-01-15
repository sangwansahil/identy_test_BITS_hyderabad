import pandas as pd
import numpy as np
from keras.layers import Dense
from keras.models import Model, Sequential
from keras import initializers

mu, sigma, size = 0, 4, 100
m, b = 0.26, 0

# here m is the slope i.e 0.12/0.45 and b is the intercept i.e 0

x = np.random.uniform(0,10, size)
df = pd.DataFrame({'x':x})

## 
df['y_perfect'] = df['x'].apply(lambda x: m*x+b)


## introducing noise
df['noise'] = np.random.normal(mu, sigma, size=(size,))
df['y'] = df['y_perfect']+df['noise']

model = Sequential([
        Dense(1, activation='linear', input_shape=(1,), kernel_initializer='glorot_uniform')
    ])


model.compile(loss='mse', optimizer='rmsprop') ## as mentioned in the question using mse and rmsprop as mentioned in the question 

## Set our learning rate to 0.01 and print it
model.optimizer.lr.set_value(.001)
print model.optimizer.lr.get_value()


history = model.fit(x=df['x'], y=df['y'], validation_split=0.2, batch_size=1, epochs=100)


## Save and print our final weights
predicted_m = model.get_weights()[0][0][0]
predicted_b = model.get_weights()[1][0]
print "\nm=%.2f b=%.2f\n" % (predicted_m, predicted_b)
