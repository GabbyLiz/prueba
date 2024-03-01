import streamlit as st
from tensorflow.keras.models import load_model
import gdown

st.title('Mi Aplicación Streamlit con Modelo Preentrenado')

# Enlace compartido de Google Drive al archivo HDF5 (reemplaza 'your_file_id')
enlace_google_drive = 'https://drive.google.com/uc?id=1uiJR1cD2W1cNVpqG77Th6XHhWSxuEVwW'

# Nombre del archivo HDF5 local (no es necesario descargarlo localmente)
nombre_archivo_local = 'modelo.hdf5'

# Descargar el modelo directamente desde el enlace de Google Drive
try:
    gdown.download(enlace_google_drive, nombre_archivo_local, quiet=False)
    modelo_cargado = load_model(nombre_archivo_local)
    st.success('Modelo cargado exitosamente.')
except Exception as e:
    st.error(f'Error al cargar el modelo: {str(e)}')
