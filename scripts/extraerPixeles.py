import os

def extraer_lineas_entre(fichero_entrada, fichero_salida):
    lineas_extraidas = []
    extrayendo = False

    with open(fichero_entrada, 'r') as archivo:
        for linea in archivo:
            if "-- PIXELS OF CLASS  0" in linea:
                extrayendo = True
                continue
            elif "-- PIXELS OF CLASS  1" in linea:
                extrayendo = False
                break

            if extrayendo:
                lineas_extraidas.append(linea.strip())

    with open(fichero_salida, 'w') as salida:
        for linea in lineas_extraidas:
            salida.write(linea + '\n')

# Obtener la ruta del directorio actual
ruta_script = os.path.dirname(os.path.abspath(__file__))

# Ruta del archivo de entrada
nombre_fichero_entrada = "IP_test.vhd"
ruta_fichero_entrada = os.path.join(ruta_script, nombre_fichero_entrada)

# Ruta del archivo de salida
nombre_fichero_salida = "pixels.txt"
ruta_fichero_salida = os.path.join(ruta_script, nombre_fichero_salida)

# Llamada a la función para extraer las líneas entre los marcadores y guardarlas en el archivo de salida
extraer_lineas_entre(ruta_fichero_entrada, ruta_fichero_salida)

print("Líneas extraídas guardadas en pixels.txt")
