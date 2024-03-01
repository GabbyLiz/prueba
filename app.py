import streamlit as st
import gdown
from tensorflow.keras.models import load_model
import os

st.title('Mi Aplicación Streamlit con Modelo Preentrenado')
# Enlace compartido de Google Drive al archivo HDF5 (reemplaza 'your_file_id')
enlace_google_drive = 'https://drive.google.com/uc?id=1uiJR1cD2W1cNVpqG77Th6XHhWSxuEVwW'

# Nombre del archivo HDF5 local
nombre_archivo_local = 'modelo.hdf5'
gdown.download(enlace_google_drive, nombre_archivo_local)
st.success('Modelo HDF5 descargado correctamente.')
ruta_archivo = "modelo.hdf5"
st.write("Ruta completa del archivo:", os.path.abspath(ruta_archivo))

ruta_archivo = "./mount/src/prueba/modelo.hdf5"
# Cargar el modelo desde el archivo HDF5
modelo_cargado = load_model(ruta_archivo)

# Mostrar información sobre el modelo

st.write('Información sobre el modelo:')
st.write(modelo_cargado.summary())

# Realizar predicciones, etc., según sea necesario con el modelo cargado
# ...

# Eliminar el archivo HDF5 después de su uso (opcional)
os.remove(nombre_archivo_local)
