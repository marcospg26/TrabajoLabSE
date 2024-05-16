import os
import re

# Función para convertir un número de punto fijo de 16 bits a flotante
def fixed_point_to_float(fixed_point_hex, fraction_bits=8):
    # Convierte el valor hexadecimal a un entero
    fixed_point_int = int(fixed_point_hex, 16)
    # Ajusta el valor si es negativo (complemento a dos)
    if fixed_point_int & (1 << 15):
        fixed_point_int -= 1 << 16
    # Convierte a flotante
    float_value = fixed_point_int / (1 << fraction_bits)
    return float_value

# Función para leer los números hexadecimales del archivo y extraer los bits del 2 al 15 y del 16 al 31
def extract_bits_and_analyze(input_file):
    max_val_2_to_15 = None
    min_val_2_to_15 = None
    max_val_16_to_31 = None
    min_val_16_to_31 = None

    with open(input_file, 'r') as f:
        for line in f:
            # Convertir el número hexadecimal a entero
            hex_number = int(line.strip(), 16)
            
            # Extraer los bits del 2 al 15 (incluidos)
            bits_2_to_15 = (hex_number >> 2) & 0x3FFF
            # Actualizar el máximo y mínimo para los bits del 2 al 15
            if max_val_2_to_15 is None or bits_2_to_15 > max_val_2_to_15:
                max_val_2_to_15 = bits_2_to_15
            if min_val_2_to_15 is None or bits_2_to_15 < min_val_2_to_15:
                min_val_2_to_15 = bits_2_to_15
            
            # Extraer los bits del 16 al 31 (incluidos)
            bits_16_to_31 = (hex_number >> 16) & 0xFFFF
            # Interpretar los bits del 16 al 31 como un valor con signo de 16 bits y convertir a flotante
            leaf_value_float = fixed_point_to_float(hex(bits_16_to_31))
            # Actualizar el máximo y mínimo para los bits del 16 al 31
            if max_val_16_to_31 is None or leaf_value_float > max_val_16_to_31:
                max_val_16_to_31 = leaf_value_float
            if min_val_16_to_31 is None or leaf_value_float < min_val_16_to_31:
                min_val_16_to_31 = leaf_value_float
            
    return (max_val_2_to_15, min_val_2_to_15), (max_val_16_to_31, min_val_16_to_31)

# Obtener la ruta del directorio actual
current_directory = os.path.dirname(os.path.abspath(__file__))

# Ruta del archivo 'nodosHoja.txt'
input_file_path = os.path.join(current_directory, 'nodosHoja.txt')

# Llamar a la función para extraer y analizar los bits
max_min_2_to_15, max_min_16_to_31 = extract_bits_and_analyze(input_file_path)

# Función para convertir un entero a una cadena hexadecimal con formato
def int_to_hex_string(number):
    return hex(number)

# Imprimir resultados
print("Máximo y mínimo en los bits del 2 al 15 (dirección del siguiente árbol):", 
      (int_to_hex_string(max_min_2_to_15[0]), int_to_hex_string(max_min_2_to_15[1])))
print("Máximo y mínimo en los bits del 16 al 31 (valor de la hoja, como flotante):", 
      (max_min_16_to_31[0], max_min_16_to_31[1]))
