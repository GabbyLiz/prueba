import streamlit as st
import gdown
from tensorflow.keras.models import load_model
import os

# Enlace compartido de Google Drive al archivo HDF5 (reemplaza 'your_file_id')
enlace_google_drive = 'https://drive.google.com/uc?id=1uiJR1cD2W1cNVpqG77Th6XHhWSxuEVwW'

# Nombre del archivo HDF5 local
nombre_archivo_local = 'modelo.hdf5'

# Descargar el archivo desde Google Drive
with st.spinner('Descargando modelo HDF5...'):
    gdown.download(enlace_google_drive, nombre_archivo_local)
    st.success('Modelo HDF5 descargado correctamente.')

# Cargar el modelo desde el archivo HDF5
modelo_cargado = load_model(nombre_archivo_local)

# Mostrar información sobre el modelo
st.title('Mi Aplicación Streamlit con Modelo Preentrenado')
st.write('Información sobre el modelo:')
st.write(modelo_cargado.summary())

# Realizar predicciones, etc., según sea necesario con el modelo cargado
# ...

# Eliminar el archivo HDF5 después de su uso (opcional)
os.remove(nombre_archivo_local)
