import streamlit as st
from tensorflow.keras.models import load_model
import gdown
import os

st.title('Mi Aplicación Streamlit con Modelo Preentrenado')

# Enlace compartido de Google Drive al archivo HDF5 (reemplaza 'your_file_id')
enlace_google_drive = 'https://drive.google.com/uc?id=1uiJR1cD2W1cNVpqG77Th6XHhWSxuEVwW'

# Nombre del archivo HDF5 local
nombre_archivo_local = 'modelo.hdf5'

# Descargar el modelo desde Google Drive en tiempo real
gdown.download(enlace_google_drive, nombre_archivo_local, quiet=False)

# Cargar el modelo
modelo_cargado = load_model(nombre_archivo_local)

# Hacer predicciones o cualquier otra cosa con el modelo cargado
# ...

# Mostrar información sobre el modelo
st.write("Modelo cargado exitosamente:", modelo_cargado.summary())
