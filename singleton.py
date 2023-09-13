import tkinter as tk

# Clase Lavadora (Singleton)


class Lavadora:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Lavadora, cls).__new__(cls)
            cls._instance.reservas = []
        return cls._instance

    def reservar_lavadora(self, fecha, hora, persona, pedido):
        self.reservas.append((fecha, hora, persona, pedido))

# Función para registrar una reserva


def reservar(pedido, nombre, fecha, hora):
    lavadora = Lavadora()
    lavadora.reservar_lavadora(pedido, nombre, fecha, hora)
    actualizar_lista_reservas()

# Función para mostrar las reservas en el cuadro de texto


def actualizar_lista_reservas():
    lavadora = Lavadora()
    lista_reservas.delete(0, tk.END)
    for reserva in lavadora.reservas:
        lista_reservas.insert(
            tk.END, f"Pedido: {reserva[0]}, Nombre: {reserva[1]}, Fecha: {reserva[2]}, Hora: {reserva[3]}")


# Configuración de la ventana principal
root = tk.Tk()
root.title("Reserva de Lavadora")
root.geometry("600x200")

# Botón 1 - Pedido 1


def boton1():
    nombre = "Juan Roque"
    fecha = "21/12/2023"
    hora = "13:15"
    pedido = "Pedido 1"
    reservar(pedido, nombre, fecha, hora)


boton_pedido1 = tk.Button(root, text="Boton 1", command=boton1)
boton_pedido1.pack()

# Botón 2 - Pedido 2


def boton2():
    nombre = "Mariano Fernandez"
    fecha = "22/12/2023"
    hora = "12:20"
    pedido = "Pedido 2"
    reservar(pedido, nombre, fecha, hora)


boton_pedido2 = tk.Button(root, text="Boton 2", command=boton2)
boton_pedido2.pack()

# Botón 3 - Pedido 3


def boton3():
    nombre = "Laura Gomez"
    fecha = "23/12/2023"
    hora = "14:30"
    pedido = "Pedido 3"
    reservar(pedido, nombre, fecha, hora)


boton_pedido3 = tk.Button(root, text="Boton 3", command=boton3)
boton_pedido3.pack()

# Botón 4 - Pedido 4


def boton4():
    nombre = "Carlos Sanchez"
    fecha = "24/12/2023"
    hora = "10:45"
    pedido = "Pedido 4"
    reservar(pedido, nombre, fecha, hora)


boton_pedido4 = tk.Button(root, text="Boton 4", command=boton4)
boton_pedido4.pack()

# Cuadro de texto para mostrar las reservas
lista_reservas = tk.Listbox(root, width=70, height=10)
lista_reservas.pack()

# Actualizar la lista de reservas al iniciar la aplicación
actualizar_lista_reservas()

root.mainloop()
