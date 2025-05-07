import pandas as pd

# Alfabeto en español con ñ
alfabeto = "abcdefghijklmnñopqrstuvwxyz"

# Cifrado César (para cifrar y descifrar con desplazamiento)
def cifrar_cesar(texto, desplazamiento):
    resultado = ""
    for char in texto:
        if char.lower() in alfabeto:
            es_mayus = char.isupper()
            index = alfabeto.index(char.lower())
            new_index = (index + desplazamiento) % len(alfabeto)
            nuevo_char = alfabeto[new_index]
            resultado += nuevo_char.upper() if es_mayus else nuevo_char
        else:
            resultado += char
    return resultado

# Lista de 10 mensajes
mensajes = [
    "hola mundo",
    "bootcamp",
    "ciberseguridad",
    "cesar",
    "programacion",
    "python",
    "inteligencia artificial",
    "cifrado",
    "seguridad",
    "datos"
]

# Lista de claves (desplazamientos)
claves = [4, 6, 20, 12, 8, 1, 5, 15, 3, 7]

# Crear la tabla con los datos
datos = []
for i in range(10):
    original = mensajes[i]
    clave = claves[i]
    cifrado = cifrar_cesar(original, clave)
    descifrado = cifrar_cesar(cifrado, -clave)  # Deshacer el cifrado
    datos.append({
        "msj_original": original,
        "clave": clave,
        "msj_cifrado": cifrado,
        "msj_descifrado": descifrado
    })

df = pd.DataFrame(datos)

# Mostrar la tabla
print(df)
