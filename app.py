import streamlit as st
import gdown
from tensorflow.keras.models import load_model
import os

st.title('Mi Aplicación Streamlit con Modelo Preentrenado')

# Enlace compartido de Google Drive al archivo HDF5 (reemplaza 'your_file_id')
enlace_google_drive = 'https://drive.google.com/uc?id=1uiJR1cD2W1cNVpqG77Th6XHhWSxuEVwW'

# Nombre del archivo HDF5 local
nombre_archivo_local = 'modelo.hdf5'

# Comprobar si el modelo ya está descargado
if not os.path.isfile(nombre_archivo_local):
    st.info('Descargando el modelo...')
    try:
        gdown.download(enlace_google_drive, nombre_archivo_local, quiet=False)
        st.success('Modelo descargado exitosamente.')
    except Exception as e:
        st.error(f'Error al descargar el modelo: {str(e)}')
else:
    st.info('El modelo ya está descargado.')

# Obtener la ruta completa del archivo
ruta_archivo = os.path.abspath(nombre_archivo_local)
st.write("Ruta completa del archivo:", ruta_archivo)

# Intentar cargar el modelo directamente desde el archivo HDF5
try:
    st.info('Cargando el modelo...')
    modelo_cargado = load_model(nombre_archivo_local)
    st.success('Modelo cargado exitosamente.')
except Exception as e:
    st.error(f'Error al cargar el modelo: {str(e)}')
