import streamlit as st
import gdown
from tensorflow.keras.models import load_model

st.title('Mi Aplicación Streamlit con Modelo Preentrenado')

# Enlace compartido de Google Drive al archivo HDF5 (reemplaza 'your_file_id')
enlace_google_drive = 'https://drive.google.com/uc?id=1uiJR1cD2W1cNVpqG77Th6XHhWSxuEVwW'

# Nombre del archivo HDF5 local
nombre_archivo_local = 'modelo.hdf5'

# Comprobar si el modelo ya está descargado
if not st.file_uploader("Cargar modelo", type=["h5"]):
    st.info('Descargando el modelo...')
    try:
        gdown.download(enlace_google_drive, nombre_archivo_local, quiet=False)
        st.success('Modelo descargado exitosamente.')
    except Exception as e:
        st.error(f'Error al descargar el modelo: {str(e)}')
else:
    st.info('El modelo ya está descargado.')

# Intentar cargar el modelo directamente desde el archivo HDF5
try:
    st.info('Cargando el modelo...')
    modelo_cargado = load_model(nombre_archivo_local)
    st.success('Modelo cargado exitosamente.')
except Exception as e:
    st.error(f'Error al cargar el modelo: {str(e)}')
