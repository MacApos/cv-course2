import plotly.graph_objects as go
import plotly.offline as po
from plotly.subplots import make_subplots
from datetime import datetime
import pandas as pd
import argparse
import pickle
import os

from architecture import models

import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.callbacks import ModelCheckpoint
from tensorflow.keras.optimizers import Adam

import warnings
warnings.filterwarnings("ignore", category=FutureWarning)
os.environ['TFF_CPP_MIN_LOG_LEVEL'] = '3'

ap = argparse.ArgumentParser()
ap.add_argument('-e', '--epochs', default=1, help='Specify number of epochs', type=int)
args = vars(ap.parse_args())

model_name = 'LeNet5'
learning_rate = 0.001
epochs = args['epochs']
batch_size = 32
input_shape = (150, 150, 3)
train_dir = r'F:\PycharmProjects\cv-course2\06_classification\image\train'
valid_dir = r'F:\PycharmProjects\cv-course2\06_classification\image\valid'


def plot_hist(history, filename):
    hist = pd.DataFrame(history.history)
    hist['epoch'] = history.epoch

    fig = make_subplots(rows=2, cols=1, subplot_titles=('Accuracy', 'Loss'))
    fig.add_trace(go.Scatter(x=hist['epoch'], y=hist['accuracy'], name='train_accuracy',
                             mode='markers+lines'), row=1, col=1)
    fig.add_trace(go.Scatter(x=hist['epoch'], y=hist['loss'], name='train_loss',
                             mode='markers+lines'), row=1, col=1)
    fig.add_trace(go.Scatter(x=hist['epoch'], y=hist['accuracy'], name='valid_loss',
                             mode='markers+lines'), row=2, col=1)
    fig.add_trace(go.Scatter(x=hist['epoch'], y=hist['loss'], name='valid_loss',
                             mode='markers+lines'), row=2, col=1)

    fig.update_xaxes(title_text='Liczba epok', row=1, col=1)
    fig.update_xaxes(title_text='Liczba epok', row=2, col=1)
    fig.update_xaxes(title_text='Accuracy', row=1, col=1)
    fig.update_xaxes(title_text='Loss', row=2, col=1)
    fig.update_layout(width=1400, height=1000, title=f'Metrics: {model_name}')

    po.plot(fig, filename=filename, auto_open=False)


train_datagen = ImageDataGenerator(
    rotation_range=30,
    rescale=1./255.,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest'
)

valid_datagen = ImageDataGenerator(rescale=1./255.)

train_generator = train_datagen.flow_from_directory(
    directory=train_dir,
    target_size=input_shape[:2],
    batch_size=batch_size,
    class_mode='binary'
)

valid_generator = valid_datagen.flow_from_directory(
    directory=valid_dir,
    target_size=input_shape[:2],
    batch_size=batch_size,
    class_mode='binary'
)

architectures = {model_name: models.LeNet5}
architecture = architectures[model_name](input_shape=input_shape)
model = architecture.build()

model.compile(
    optimizer=Adam(learning_rate=learning_rate),
    loss='binary_crossentropy',
    metrics=['accuracy']
)

model.summary()

dt = datetime.now().strftime('%d_%m_%Y_%H_%M')
filepath = os.path.join('output', 'model_'+dt+'.hdf5')
checkpoint = ModelCheckpoint(filepath=filepath, monitor='val_accuracy', save_best_only=True)

history = model.fit_generator(
    generator=train_generator,
    steps_per_epoch=train_generator.samples//batch_size,
    validation_data=valid_generator,
    validation_steps=valid_generator.samples//batch_size,
    epochs=epochs,
    callbacks=[checkpoint]
)

print('Eksport wykresu do pliku html...')
filename = os.path.join('output', 'model_'+dt+'.html')
plot_hist(history=history, filename=filename)

print('Eksport etykiet do pliku...')
with open('output\label.pickle', 'wb') as file:
    file.write(pickle.dumps(train_generator.calss_indices))
