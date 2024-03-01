import streamlit as st
from tensorflow.keras.models import load_model
import gdown
import os

st.title('Mi Aplicación Streamlit con Modelo Preentrenado')

# Enlace compartido de Google Drive al archivo HDF5 (reemplaza 'your_file_id')
enlace_google_drive = 'https://drive.google.com/uc?id=1uiJR1cD2W1cNVpqG77Th6XHhWSxuEVwW'

# Nombre del archivo HDF5 local (no es necesario descargarlo localmente)
nombre_archivo_local = 'modelo.hdf5'

# Comprobar si el modelo ya está descargado
if not os.path.exists(nombre_archivo_local):
    st.info('Descargando el modelo...')
    try:
        gdown.download(enlace_google_drive, nombre_archivo_local, quiet=False)
        st.success('Modelo descargado exitosamente.')
    except Exception as e:
        st.error(f'Error al descargar el modelo: {str(e)}')
else:
    st.info('El modelo ya está descargado.')

# Comprobar el contenido del directorio actual
contenido_directorio = os.listdir()
st.write('Contenido del directorio actual:', contenido_directorio)

# Intentar cargar el modelo
try:
    modelo_cargado = load_model(nombre_archivo_local)
    st.success('Modelo cargado exitosamente.')
except Exception as e:
    st.error(f'Error al cargar el modelo: {str(e)}')
