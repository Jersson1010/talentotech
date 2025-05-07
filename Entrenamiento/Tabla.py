import pandas as pd # type: ignore

# Crear la tabla (DataFrame)
data = {
    "ID_Empleado": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    "Nombre": ["Laura", "Carlos", "Marta", "Luis", "Diana", "Pedro", "Ana", "Jorge", "Camila", "Felipe"],
    "Departamento": ["Ventas", "TI", "Contabilidad", "Marketing", "TI", "Recursos Humanos", "Ventas", "Marketing", "TI", "Contabilidad"],
    "Salario": [3200000, 4500000, 3900000, 4100000, 4700000, 3600000, 3300000, 4000000, 4800000, 3700000]
}

tabla_empleados = pd.DataFrame(data)

# Mostrar la tabla
print(tabla_empleados)
