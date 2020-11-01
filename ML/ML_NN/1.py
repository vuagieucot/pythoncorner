import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

data = keras.datasets.fashion_mnist

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

(train_images, train_labels),(test_images, test_labels) = data.load_data()

train_images = train_images/255.0
test_images = test_images/255.0

model = keras.Sequential([
    keras.players.Flatten(input_shape=(28,28)),
    keras.layers.Dense(128, activation="relu"),
    keras.layers.Dense(10, activation="softmax")
    ])

model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics = ["accuracy"])

model.fit(train_images, train_labels, epochs=5)

test_loss, tess_acc= model.evaluate(test_images, test_labels)
print("Accuracy: {}\nLoss: {}".format(test_loss, tess_acc))
