import streamlit as st
import gdown
from tensorflow.keras.models import load_model

st.title('Mi Aplicación Streamlit con Modelo Preentrenado')
enlace_google_drive = 'https://drive.google.com/uc?id=1uiJR1cD2W1cNVpqG77Th6XHhWSxuEVwW'
nombre_archivo_local = 'modelo.hdf5'

# Descargar el modelo cada vez que se ejecuta la aplicación
gdown.download(enlace_google_drive, nombre_archivo_local, quiet=False)
st.success('Modelo HDF5 descargado correctamente.')

# Intentar cargar el modelo
try:
    modelo_cargado = load_model(nombre_archivo_local)
    st.success('Modelo cargado exitosamente.')
except Exception as e:
    st.error(f'Error al cargar el modelo: {str(e)}')
