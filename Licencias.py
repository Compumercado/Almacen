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