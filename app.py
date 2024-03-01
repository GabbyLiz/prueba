import streamlit as st
import gdown
import os

# Enlace directo al archivo compartido en Google Drive (reemplaza con tu enlace)
google_drive_url = "https://drive.google.com/file/d/1uiJR1cD2W1cNVpqG77Th6XHhWSxuEVwW/view?usp=drive_link"

# Función para descargar y almacenar en caché el modelo
@st.cache(suppress_st_warning=True)
def descargar_y_cargar_modelo(url, nombre_archivo):
    # Descargar el modelo desde Google Drive
    st.text(f"Descargando modelo desde {url}...")
    gdown.download(url, nombre_archivo, quiet=False)

    # Cargar el modelo utilizando la biblioteca correspondiente (reemplaza según tu modelo)
    # Ejemplo con TensorFlow / Keras:
    # from tensorflow.keras.models import load_model
    # modelo = load_model(nombre_archivo)

    # Retornar el modelo
    return modelo

# Función para obtener el peso del archivo descargado
def obtener_peso_del_archivo(archivo):
    return os.path.getsize(archivo)

# Nombre del archivo a descargar y cargar
nombre_archivo = "modelo.hdf5"

# Botón en Streamlit para iniciar la descarga y carga del modelo
if st.button("Descargar y Cargar Modelo desde Google Drive"):
    # Llamada a la función para descargar y cargar el modelo
    modelo = descargar_y_cargar_modelo(google_drive_url, nombre_archivo)
    st.success("Descarga y carga del modelo exitosas.")

    # Mostrar el peso del archivo descargado
    peso_del_archivo = obtener_peso_del_archivo(nombre_archivo)
    st.text(f"Peso del archivo descargado: {peso_del_archivo} bytes.")
