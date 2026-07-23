print("Hola mundofghy")
import streamlit as st

# Configura el título de la pestaña del navegador
st.set_page_config(page_title="Mi Primera App", layout="wide")

# Título y texto en la página principal
st.title("¡Bienvenido a mi interfaz de Streamlit!")
st.write("Esta es una aplicación web interactiva construida completamente en Python.")

# --- Barra lateral (Sidebar) ---
st.sidebar.header("Opciones de Configuración")

# Widget: Cuadro de texto
usuario = st.sidebar.text_input("¿Cuál es tu nombre?")

# Widget: Deslizador (Slider)
edad = st.sidebar.slider("Selecciona tu edad", 18, 99, 25)

# --- Interacción ---
if st.sidebar.button("Saludar"):
    st.success(f"¡Hola {usuario}! Tienes {edad} años.")
