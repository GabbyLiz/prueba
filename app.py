import streamlit as st
import gdown
from tensorflow.keras.models import load_model
import os

st.title('Mi Aplicación Streamlit con Modelo Preentrenado')
enlace_google_drive = 'https://drive.google.com/uc?id=1uiJR1cD2W1cNVpqG77Th6XHhWSxuEVwW'
nombre_archivo_local = 'modelo.hdf5'

# Descargar el modelo solo si no está presente
if not os.path.exists(nombre_archivo_local):
    gdown.download(enlace_google_drive, nombre_archivo_local)
    st.success('Modelo HDF5 descargado correctamente.')

ruta_archivo = "modelo.hdf5"
ruta_completa = os.path.join(os.path.dirname(__file__), ruta_archivo)

st.write("Ruta completa del archivo:", ruta_completa)

# Intentar cargar el modelo
try:
    modelo_cargado = load_model(ruta_completa)
    st.success('Modelo cargado exitosamente.')
except Exception as e:
    st.error(f'Error al cargar el modelo: {str(e)}')
