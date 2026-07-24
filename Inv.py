def mostrar_menu():
    print("\n--- Control de Inventario ---")
    print("1. Agregar o actualizar producto")
    print("2. Ver inventario")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")

def gestionar_inventario():
    inventario = {}
    
    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-5): ")
        
        if opcion == '1':
            nombre = input("Nombre del producto: ").strip().lower()
            try:
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio unitario ($): "))
                inventario[nombre] = {"cantidad": cantidad, "precio": precio}
                print(f"¡Producto '{nombre}' guardado con éxito!")
            except ValueError:
                print("Error: Ingresa números válidos para cantidad y precio.")
                
        elif opcion == '2':
            if not inventario:
                print("El inventario está vacío.")
            else:
                print("\n--- Lista de Productos ---")
                for prod, datos in inventario.items():
                    print(f"- {prod.capitalize()}: {datos['cantidad']} unidades | ${datos['precio']:.2f} c/u")
                    
        elif opcion == '3':
            nombre = input("Nombre del producto a buscar: ").strip().lower()
            if nombre in inventario:
                datos = inventario[nombre]
                print(f"Encontrado -> {nombre.capitalize()}: {datos['cantidad']} unidades | ${datos['precio']:.2f} c/u")
            else:
                print("El producto no existe en el inventario.")
                
        elif opcion == '4':
            nombre = input("Nombre del producto a eliminar: ").strip().lower()
            if nombre in inventario:
                del inventario[nombre]
                print(f"Producto '{nombre}' eliminado.")
            else:
                print("El producto no fue encontrado.")
                
        elif opcion == '5':
            print("Saliendo del sistema de inventario...")
            break
        else:
            print("Opción no válida. Elige un número del 1 al 5.")

if __name__ == "__main__":
    gestionar_inventario()