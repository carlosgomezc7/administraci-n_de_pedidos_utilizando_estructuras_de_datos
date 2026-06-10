import tkinter as tk

# Creamos la ventana principal
ventana = tk.Tk()
ventana.title("Sistema de Gestión de Pedidos")
ventana.geometry("400x300")

# Etiqueta de saludo
etiqueta = tk.Label(
    ventana, text="Seleccione una estructura de datos para gestionar los pedidos:")
etiqueta.pack(pady=10)

# Botones básicos
boton_pila = tk.Button(ventana, text="Pila")
boton_pila.pack()
boton_cola = tk.Button(ventana, text="Cola")
boton_cola.pack()
boton_lista = tk.Button(ventana, text="Lista")
boton_lista.pack()

ventana.mainloop()
