
import streamlit as st

# Configura el título de la pestaña del navegador
st.set_page_config(page_title="Hola Mundo", layout="wide")

# Título y texto en la página principal
st.title("¡Inventario de Almacen!")
st.write("Esta es una aplicación web interactiva construida completamente en Python.")

# --- Barra lateral (Sidebar) ---
st.sidebar.header("Menu de Opciones")

# Widget: Cuadro de texto
usuario = st.sidebar.text_input(" ")

# Widget: Deslizador (Slider)
edad = st.sidebar.slider("Selecciona tu edad", 18, 99, 25)

# --- Interacción ---
if st.sidebar.button("Saludar"):
    st.success(f"¡Hola {usuario}! Tienes {edad} años.")
