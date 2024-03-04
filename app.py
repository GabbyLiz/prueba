import streamlit as st
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Crear un modelo Keras simple (sin entrenar)
def create_model():
    model = Sequential()
    model.add(Dense(units=1, input_dim=1, activation='linear'))
    model.compile(optimizer='adam', loss='mean_squared_error')
    return model

# Función para predecir el cuadrado y el cubo de un número
def predict_numbers(model, number):
    square = model.predict(tf.constant([number]))[0, 0] ** 2
    cube = model.predict(tf.constant([number]))[0, 0] ** 3
    return square, cube

# Streamlit UI
st.title('Number Transformation App')

# Crear el modelo
model = create_model()

# Entrada de usuario para el número
number = st.number_input('Enter a number:', value=1.0, step=0.1)

# Botón para predecir
if st.button('Predict'):
    # Realizar la predicción
    square, cube = predict_numbers(model, number)

    # Mostrar los resultados
    st.header('Results:')
    st.write(f'Square of {number}: {square:.4f}')
    st.write(f'Cube of {number}: {cube:.4f}')
