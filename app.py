import streamlit as st
import gdown
import os
import h5py
import numpy as np

st.title('Mi Aplicación Streamlit con Modelo Preentrenado')

# Enlace compartido de Google Drive al archivo HDF5 (reemplaza 'your_file_id')
enlace_google_drive = 'https://drive.google.com/uc?id=1uiJR1cD2W1cNVpqG77Th6XHhWSxuEVwW'

# Nombre del archivo HDF5 local
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

# Intentar cargar el modelo directamente desde el archivo HDF5
try:
    with h5py.File(nombre_archivo_local, 'r') as file:
        # Obtener la arquitectura, pesos y configuración del modelo
        st.info('Cargando la arquitectura, los pesos y la configuración del modelo...')
        model_config = file.attrs.get('model_config')
        if model_config is None:
            st.error('No se encontró la configuración del modelo en el archivo HDF5.')
        else:
            model_config = json.loads(model_config.decode('utf-8'))
            loaded_model = model_from_config(model_config)

            # Cargar los pesos del modelo
            st.info('Cargando los pesos del modelo...')
            loaded_model.load_weights('model_weights')

            st.success('Modelo cargado exitosamente.')
except Exception as e:
    st.error(f'Error al cargar el modelo: {str(e)}')
