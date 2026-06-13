from estructura import GestorPedidos
from menus import menu_principal, menu_operaciones


def ejecutar():
    tipos = {'1': 'pila', '2': 'cola', '3': 'lista'}

    while True:
        opcion_estr = menu_principal()
        if opcion_estr in tipos:
            break
        print("Opción no válida. Intente de nuevo.")

    gestor = GestorPedidos(tipos[opcion_estr])

    while True:
        op = menu_operaciones()

        if op == '1':
            prod = input("Nombre del producto: ")
            gestor.agregar(prod)
        elif op == '2':
            pos = None
            if gestor.tipo == 'lista':
                print(gestor.mostrar())
                try:
                    pos = int(input("Ingrese la posición a atender: "))
                except ValueError:
                    print("Error: Debe ingresar un número entero.")
                    continue
            print("\n" + gestor.atender(pos))
        elif op == '3':
            print("\nPedidos actuales:\n" + gestor.mostrar())
        elif op == '4':
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    ejecutar()
