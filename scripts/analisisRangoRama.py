# Extraer los bits del 8 al 23 de los números hexadecimales en un archivo y 
# encontrar el máximo y mínimo

import os

# Función para leer los números hexadecimales del archivo y extraer los bits del 8 al 23,
# del 1 al 7 y del 24 al 31
def extract_bits_and_analyze(input_file):
    max_val_8_to_23 = None
    min_val_8_to_23 = None
    max_val_1_to_7 = None
    min_val_1_to_7 = None
    max_val_24_to_31 = None
    min_val_24_to_31 = None
    with open(input_file, 'r') as f:
        for line in f:
            # Convertir el número hexadecimal a entero
            hex_number = int(line.strip(), 16)
            # Extraer los bits del 8 al 23 (incluidos)
            bits_8_to_23 = (hex_number >> 8) & 0xFFFF
            # Actualizar el máximo y mínimo para los bits del 8 al 23
            if max_val_8_to_23 is None or bits_8_to_23 > max_val_8_to_23:
                max_val_8_to_23 = bits_8_to_23
            if min_val_8_to_23 is None or bits_8_to_23 < min_val_8_to_23:
                min_val_8_to_23 = bits_8_to_23
            
            # Extraer los bits del 1 al 7 (incluidos)
            bits_1_to_7 = (hex_number >> 1) & 0x7F
            # Actualizar el máximo y mínimo para los bits del 1 al 7
            if max_val_1_to_7 is None or bits_1_to_7 > max_val_1_to_7:
                max_val_1_to_7 = bits_1_to_7
            if min_val_1_to_7 is None or bits_1_to_7 < min_val_1_to_7:
                min_val_1_to_7 = bits_1_to_7
            
            # Extraer los bits del 24 al 31 (incluidos)
            bits_24_to_31 = hex_number >> 24
            # Actualizar el máximo y mínimo para los bits del 24 al 31
            if max_val_24_to_31 is None or bits_24_to_31 > max_val_24_to_31:
                max_val_24_to_31 = bits_24_to_31
            if min_val_24_to_31 is None or bits_24_to_31 < min_val_24_to_31:
                min_val_24_to_31 = bits_24_to_31
            
    return (max_val_8_to_23, min_val_8_to_23), (max_val_1_to_7, min_val_1_to_7), (max_val_24_to_31, min_val_24_to_31)

# Obtener la ruta del directorio actual
current_directory = os.path.dirname(os.path.abspath(__file__))

# Ruta del archivo 'nodosRama.txt'
input_file_path = os.path.join(current_directory, 'nodosRama.txt')

# Llamar a la función para extraer y analizar los bits
max_min_8_to_23, max_min_1_to_7, max_min_24_to_31 = extract_bits_and_analyze(input_file_path)

# Función para convertir un entero a una cadena hexadecimal con formato
def int_to_hex_string(number):
    return hex(number)

# Imprimir resultados en hexadecimal
print("Máximo y mínimo en los bits del 1 al 7 (dist. nodo derch.):",
      (int_to_hex_string(max_min_1_to_7[0]), int_to_hex_string(max_min_1_to_7[1])))
print("Máximo y mínimo en los bits del 8 al 23 (valor cmp):",
      (int_to_hex_string(max_min_8_to_23[0]), int_to_hex_string(max_min_8_to_23[1])))
print("Máximo y mínimo en los bits del 24 al 31 (feature):",
      (int_to_hex_string(max_min_24_to_31[0]), int_to_hex_string(max_min_24_to_31[1])))


