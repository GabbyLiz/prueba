import streamlit as st
import gdown
from tensorflow.keras.models import load_model
import os

# Enlace compartido de Google Drive al archivo HDF5 (reemplaza 'your_file_id')
enlace_google_drive = 'https://drive.google.com/uc?id=1uiJR1cD2W1cNVpqG77Th6XHhWSxuEVwW'

# Nombre del archivo HDF5 local
nombre_archivo_local = 'modelo.hdf5'
gdown.download(enlace_google_drive, nombre_archivo_local)
st.success('Modelo HDF5 descargado correctamente.')
ruta_archivo = "modelo.hdf5"
st.write("Ruta completa del archivo:", os.path.abspath(ruta_archivo))
