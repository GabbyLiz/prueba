import streamlit as st
import gdown
from tensorflow.keras.models import load_model
import os

# Enlace compartido de Google Drive al archivo HDF5 (reemplaza 'your_file_id')
enlace_google_drive = 'https://drive.google.com/uc?id=1uiJR1cD2W1cNVpqG77Th6XHhWSxuEVwW'

# Nombre del archivo HDF5 local
nombre_archivo_local = 'modelo.hdf5'
st.success("Ruta completa del archivo:", os.path.abspath(ruta_archivo))
