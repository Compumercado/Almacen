import streamlit as st
import pandas as pd
import numpy as np

st.title('Uber pickups in NYC')

(base) lf-mac-0250:~ alastairhayes$ streamlit hello

  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://172.20.10.2:8501




import datetime
import getpass

# Obtener fecha actual y usuario del sistema
fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
usuario_actual = getpass.getuser()

# Crear el diccionario con los datos de la empresa
datos_empresa = {
    "empresa": "Mi Empresa S.A.",
    "fecha": fecha_actual,
    "numero_serie": "SN-2026-9876",
    "usuario": usuario_actual
}

print(datos_empresa)