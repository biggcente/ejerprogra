class Reserva:
    def __init__(self, nombre_del_pasajero, número_de_vuelo, fecha):
        self.nombre_del_pasajero = nombre_del_pasajero
        self.numero_de_vuelo = número_de_vuelo
        self.fecha = fecha
        
    def mostrar_detalle(self):
        return f"Nombre del pasajero: {self.nombre_del_pasajero}, numero de vuelo: {self.numero_de_vuelo}, fecha: {self.fecha}"
    
class ReservaEconómica(Reserva):
    def __init__(self, nombre_del_pasajero, número_de_vuelo, fecha, precio):
        super().__init__(nombre_del_pasajero, número_de_vuelo, fecha)
        self.precio = precio


    def mostrar_detalle(self):
        detalle_padre = super().mostrar_detalle()
        return f"{detalle_padre}, precio: {self.precio}"
    
class ReservaBusiness(Reserva):
    def __init__(self, nombre_del_pasajero, número_de_vuelo, fecha, precio):
        super().__init__(nombre_del_pasajero, número_de_vuelo, fecha)
        self.precio = precio


    def mostrar_detalle(self):
        detalle_padre = super().mostrar_detalle()
        return f"{detalle_padre}, precio: {self.precio}"
    

class ReservaPrimeraClase(Reserva):
    def __init__(self, nombre_del_pasajero, número_de_vuelo, fecha, precio):
        super().__init__(nombre_del_pasajero, número_de_vuelo, fecha)
        self.precio = precio


    def mostrar_detalle(self):
        detalle_padre = super().mostrar_detalle()
        return f"{detalle_padre}, precio: {self.precio}"
    

if __name__ == "__main__":
    pasajero1 = ReservaEconómica("vicente", 5, "26-09-2023", 10000000)
    pasajero2 = ReservaBusiness("juanfra", 2, "2023-10-15", 100000000000)
    pasajero3 = ReservaPrimeraClase("sergio", 7, "21-03-2023", 100000000000000000)

    print(pasajero1.mostrar_detalle())
    print(pasajero2.mostrar_detalle())
    print(pasajero3.mostrar_detalle())   
