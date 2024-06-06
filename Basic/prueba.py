class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def mostrar_informacion(self):
        return f"Empleado: {self.nombre}, Salario: {self.salario}"

class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento):
        super().__init__(nombre, salario)
        self.departamento = departamento

    def mostrar_informacion(self):
        info_basica = super().mostrar_informacion()
        return f"{info_basica}, Departamento: {self.departamento}"

# Crear una instancia de Gerente
mi_gerente = Gerente("Alice", 75000, "Ventas")

# Mostrar información del gerente
print(mi_gerente.mostrar_informacion())
# Imprime "Empleado: Alice, Salario: 75000, Departamento: Ventas"