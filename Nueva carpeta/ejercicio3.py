lista = []

while True:
    print("\n Lista de productos")
    print("1. Agregar producto")
    print("2. Ver lista")
    print("3. Modificar producto")
    print("4. Eliminar producto")
    print("5. Salir")

    opcion = input("Elige una opción (1-5): \n ")

    if opcion == "1":
        nuevo_producto = input("ingresa el producto:\n")
        lista.append(nuevo_producto)
        print("producto agregado con éxito.")

    elif opcion == "2":
        if lista:
            print("Contenido de la lista:")
            for i, producto in enumerate(lista):
                print(f"{i}: {producto}")
        else:
            print("La lista está vacía.")

    elif opcion == "3":
        if lista:
            for i, producto in enumerate(lista):
                print(f"{i}: {producto}")
            try:
                indice = int(input("Escribe el número del producto que quieres modificar: "))
                if 0 <= indice < len(lista):
                    nuevo_valor = input("Escribe el nuevo valor: ")
                    lista[indice] = nuevo_valor
                    print("Producto modificado con éxito.")
                else:
                    print("Índice fuera de rango.")
            except ValueError:
                print("Debes escribir un número válido.")
        else:
            print("La lista está vacía.")

    elif opcion == "4":
        if lista:
            for i, dato in enumerate(lista):
                print(f"{i}: {dato}")
            try:
                indice = int(input("Escribe el número del producto que quieres eliminar: "))
                if 0 <= indice < len(lista):
                    eliminado = lista.pop(indice)
                    print(f"Dato '{eliminado}' eliminado con éxito.")
                else:
                    print("Índice fuera de rango.")
            except ValueError:
                print("Debes escribir un número válido.")
        else:
            print("La lista está vacía.")

    elif opcion == "5":
        print("Saliste")
        break

    else:
        print("Opción no válida. Intenta de nuevo.")
