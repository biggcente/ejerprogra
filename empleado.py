class Empleado:
    def __init__(self, nombre, edad, salario):
        self.nombre = nombre
        self.edad = edad
        self.salario = salario

    def describir_rol(self):
        return f"Empleado genérico"


class Gerente(Empleado):
    def __init__(self, nombre, edad, salario, departamento):
        super().__init__(nombre, edad, salario)
        self.departamento = departamento

    def describir_rol(self):
        return f"Gerente en el departamento de {self.departamento}"


class Ingeniero(Empleado):
    def __init__(self, nombre, edad, salario, especialidad):
        super().__init__(nombre, edad, salario)
        self.especialidad = especialidad

    def describir_rol(self):
        return f"Ingeniero especializado en {self.especialidad}"


class Asistente(Empleado):
    def __init__(self, nombre, edad, salario, supervisor):
        super().__init__(nombre, edad, salario)
        self.supervisor = supervisor

    def describir_rol(self):
        return f"Asistente de {self.supervisor}"


if __name__ == "__main__":
    empleado1 = Empleado("Juan", 30, 40000)
    gerente1 = Gerente("Ana", 40, 60000, "Ventas")
    ingeniero1 = Ingeniero("Carlos", 28, 55000, "Desarrollo Web")
    asistente1 = Asistente("María", 25, 35000, "asistente de ventas")

    print(f"{empleado1.nombre}: {empleado1.describir_rol()}")
    print(f"{gerente1.nombre}: {gerente1.describir_rol()}")
    print(f"{ingeniero1.nombre}: {ingeniero1.describir_rol()}")
    print(f"{asistente1.nombre}: {asistente1.describir_rol()}")