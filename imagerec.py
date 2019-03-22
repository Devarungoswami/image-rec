import tensorflow as tf
mnist =tf.keras.datasets.mnist


import tensorflow as tf
mnist =tf.keras.datasets.mnist


(x_train,y_train),(x_test,y_test)=mnist.load_data()
x_train= tf.keras.utils.normalize(x_train,axis=1)
x_test= tf.keras.utils.normalize(x_test,axis=1)


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
plt.imshow(x_train[0], cmap=plt.cm.binary)
plt.show()


import keras
model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(10, activation=tf.nn.softmax))

model.compile(optimizer='adam', 
loss='sparse_categorical_crossentropy',
metrics=['accuracy'])
model.fit(x_train,y_train,epochs=3)

import numpy as np

predictions=model.predict([x_test])
print(predictions)
print(np.argmax(predictions[0]))

plt.imshow(x_test[0])
plt.show()




