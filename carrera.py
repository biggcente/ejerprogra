class Carrera:
    def __init__(self, nombre, numero_corredor):
        self.nombre = nombre
        self.numero_corredor = numero_corredor


    def mostrar_detalle(self):
        return f"Nombre: {self.nombre}, su numero es: {self.numero_corredor}"
    

class Categoria(Carrera):
    def __init__(self, nombre, numero_corredor, categoria):
        super().__init__(nombre, numero_corredor)
        self.categoria = categoria

    def mostrar_detalle(self):
        detalle_padre = super().mostrar_detalle()
        return f"{detalle_padre}, corre en la categoria: {self.categoria}"
    
if __name__ == "__main__":
    corredor1 = Categoria("juanfra", 50, "mimi")

    print(corredor1.mostrar_detalle())
    

    
    
