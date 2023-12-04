# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BpOpBRIagXILA9o2SK7pkjszRrhkstHW
"""





"""Step 1: installation and Setup

"""

pip install tensorflow

import tensorflow as tf

import tensorflow as tf

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

"""Step 2: Data Preprocessing"""

from google.colab import files
uploaded = files.upload()

import pandas as pd

training_data = pd.read_csv("/content/training_set (1).csv")

training_data.head()

training_data.tail()

training_data.info()

training_set = training_data.iloc[:, 1:2].values

training_set.shape, training_data.shape

from sklearn.preprocessing import MinMaxScaler
sc = MinMaxScaler(feature_range=(0,1))
training_set_scaled = sc.fit_transform(training_set)

training_set_scaled

import numpy as np

x_train = []
y_train = []

for i in range(60, 1510):
    x_train.append(training_set_scaled[i-60:i, 0])
    y_train.append(training_set_scaled[i, 0])

# Convert the Python lists to NumPy arrays after the loop
x_train = np.array(x_train)
y_train = np.array(y_train)

x_train

y_train

x_train.shape

x_train = x_train.reshape(1450, 60, 1)

x_train.shape

"""Step 3: Building LSTM"""

model = tf.keras.models.Sequential()

#first LSTM layer
model.add(tf.keras.layers.LSTM(units=60, activation='relu', return_sequences=True, input_shape=(60,1)))
#droupout layer
model.add(tf.keras.layers.Dropout(0.2))

# second LSTM layer

model.add(tf.keras.layers.LSTM(units=60, activation='relu', return_sequences=True))

#dropout layer

model.add(tf.keras.layers.Dropout(0.2))

# third LSTM layer

model.add(tf.keras.layers. LSTM(units=80, activation= 'relu', return_sequences=True))

# dropout layer

model.add(tf.keras.layers.Dropout(0.2))

#fourth LSTM layer

model.add(tf.keras.layers.LSTM(units=120, activation='relu'))

#dropout layer

model.add(tf.keras.layers.Dropout(0.2))

#output layer
model.add(tf.keras.layers.Dense(units=1))

model.summary()

#compile the model
model.compile(optimizer='adam', loss='mean_squared_error')

"""Step 4: Training the model

"""

model.fit(x_train, y_train, batch_size=32, epochs=100)



"""Step 5: Making Predictions

"""

test_data = pd.read_csv('/content/test_set (3).csv')

test_data.shape

test_data.info()

real_stock_price = test_data.iloc[:, 1:2].values

real_stock_price

real_stock_price.shape

dataset_total = pd.concat([training_data['Open'], test_data['Open']], axis=0)
inputs = dataset_total[len(dataset_total)-len(test_data)-60:].values
inputs = inputs.reshape(-1, 1)
inputs = sc.transform(inputs)
x_test = []
for i in range(60, 80):
  x_test.append(inputs[i-60:i, 0])


x_test = np.array(x_test)
x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))
predicted_stock_price = model.predict(x_test)
predicted_stock_price = sc.inverse_transform(predicted_stock_price)

print(predicted_stock_price[0]), print(real_stock_price[0])

"""Step 6: Visulization"""

plt.plot(real_stock_price, color='red', label='Real Google Stock Price')

plt.plot(predicted_stock_price, color='blue', label='Predicted Google Stock Price')

plt.title('Google Stock Price Prediction')

plt.xlabel('Time')

plt.ylabel('Google Stock Price')

plt.legend()

plt.show()