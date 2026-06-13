class GestorPedidos:
    def __init__(self, tipo):
        self.pedidos = []
        self.tipo = tipo  # 'pila', 'cola', o 'lista'

    def agregar(self, pedido):
        self.pedidos.append(pedido)

    def atender(self, posicion=None):
        if not self.pedidos:
            return "No hay pedidos pendientes."

        if self.tipo == 'pila':  # LIFO (Último en entrar, primero en salir)
            return f"Atendido: {self.pedidos.pop()}"
        elif self.tipo == 'cola':  # FIFO (Primero en entrar, primero en salir)
            return f"Atendido: {self.pedidos.pop(0)}"
        elif self.tipo == 'lista':  # Acceso por posición
            idx = posicion if posicion is not None else 0  # Por defecto atiende al primero
            if isinstance(idx, int) and 0 <= idx < len(self.pedidos):
                return f"Atendido: {self.pedidos.pop(idx)}"
            return "Posición inválida."

    def mostrar(self):
        if not self.pedidos:
            return "La lista de pedidos está vacía."
        return "\n".join([f"{i}. {p}" for i, p in enumerate(self.pedidos)])
