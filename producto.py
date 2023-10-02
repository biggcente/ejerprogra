class Producto:
    def __init__(self, nombre, precio, categoria):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria

    def mostrar_detalle(self):
        return f"Nombre: {self.nombre}, Precio: {self.precio}, Categoría: {self.categoria}"


class Electronico(Producto):
    def __init__(self, nombre, precio, categoria, marca, modelo):
        super().__init__(nombre, precio, categoria)
        self.marca = marca
        self.modelo = modelo

    def mostrar_detalle(self):
        detalle_padre = super().mostrar_detalle()
        return f"{detalle_padre}, Marca: {self.marca}, Modelo: {self.modelo}"


class Alimenticio(Producto):
    def __init__(self, nombre, precio, categoria, fecha_vencimiento):
        super().__init__(nombre, precio, categoria)
        self.fecha_vencimiento = fecha_vencimiento

    def mostrar_detalle(self):
        detalle_padre = super().mostrar_detalle()
        return f"{detalle_padre}, Fecha de Vencimiento: {self.fecha_vencimiento}"


class Vestimenta(Producto):
    def __init__(self, nombre, precio, categoria, talla, color):
        super().__init__(nombre, precio, categoria)
        self.talla = talla
        self.color = color

    def mostrar_detalle(self):
        detalle_padre = super().mostrar_detalle()
        return f"{detalle_padre}, Talla: {self.talla}, Color: {self.color}"



if __name__ == "__main__":
    producto1 = Electronico("Teléfono", 500000 , "Electrónico", "Samsung", "Galaxy S20")
    producto2 = Alimenticio("Leche", 2000 , "Alimenticio", "2023-10-15")
    producto3 = Vestimenta("Camiseta", 20000 , "Vestimenta", "M", "Azul")

    print(producto1.mostrar_detalle())
    print(producto2.mostrar_detalle())
    print(producto3.mostrar_detalle())