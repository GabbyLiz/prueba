import streamlit as st
from tensorflow.keras.models import load_model
import gdown

st.title('Mi Aplicación Streamlit con Modelo Preentrenado')

# Enlace compartido de Google Drive al archivo HDF5 (reemplaza 'your_file_id')
enlace_google_drive = 'https://drive.google.com/uc?id=1uiJR1cD2W1cNVpqG77Th6XHhWSxuEVwW'

# Descargar el modelo desde Google Drive en tiempo real
modelo_cargado = load_model(gdown.cached_download(enlace_google_drive))

# Hacer predicciones o cualquier otra cosa con el modelo cargado
# ...

# Mostrar información sobre el modelo
st.write("Modelo cargado exitosamente:", modelo_cargado.summary())
