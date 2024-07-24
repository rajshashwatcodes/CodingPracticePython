import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Conv2D, MaxPooling2D, Flatten, Dense, Concatenate
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.losses import MeanSquaredError, SparseCategoricalCrossentropy

# Define input shape
input_shape = (224, 224, 3)

# Input layer
inputs = Input(shape=input_shape)

# Convolutional base
x = Conv2D(32, (3, 3), activation='relu')(inputs)
x = MaxPooling2D((2, 2))(x)
x = Conv2D(64, (3, 3), activation='relu')(x)
x = MaxPooling2D((2, 2))(x)
x = Conv2D(128, (3, 3), activation='relu')(x)
x = MaxPooling2D((2, 2))(x)
x = Flatten()(x)

# Shared dense layer
x = Dense(512, activation='relu')(x)

# Bounding box regression output
bbox_output = Dense(4, activation='linear', name='bbox_output')(x)

# Road sign classification output
road_sign_output = Dense(3, activation='softmax', name='road_sign_output')(x)

# Traffic signal classification output
traffic_signal_output = Dense(3, activation='softmax', name='traffic_signal_output')(x)

# Combine all outputs
model = Model(inputs=inputs, outputs=[bbox_output, road_sign_output, traffic_signal_output])

# Compile the model
model.compile(optimizer=Adam(),
              loss={
                  'bbox_output': MeanSquaredError(),
                  'road_sign_output': SparseCategoricalCrossentropy(),
                  'traffic_signal_output': SparseCategoricalCrossentropy()
              },
              metrics={
                  'road_sign_output': 'accuracy',
                  'traffic_signal_output': 'accuracy'
              })

# Print model summary
model.summary()

# Example data (randomly generated for illustration)
# X_train: input images, y_bbox: bounding boxes, y_road_sign: road sign labels, y_traffic_signal: traffic signal labels
X_train = np.random.random((100, 224, 224, 3))
y_bbox = np.random.random((100, 4))
y_road_sign = np.random.randint(3, size=(100,))
y_traffic_signal = np.random.randint(3, size=(100,))

# Train the model
history = model.fit(X_train, {'bbox_output': y_bbox, 'road_sign_output': y_road_sign, 'traffic_signal_output': y_traffic_signal},
                    epochs=10, batch_size=16)

# Evaluate the model
evaluation = model.evaluate(X_train, {'bbox_output': y_bbox, 'road_sign_output': y_road_sign, 'traffic_signal_output': y_traffic_signal})
print(f"Evaluation results: {evaluation}")
