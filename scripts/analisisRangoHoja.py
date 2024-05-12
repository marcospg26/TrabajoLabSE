import os

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
            # Actualizar el máximo y mínimo para los bits del 16 al 31
            if max_val_16_to_31 is None or bits_16_to_31 > max_val_16_to_31:
                max_val_16_to_31 = bits_16_to_31
            if min_val_16_to_31 is None or bits_16_to_31 < min_val_16_to_31:
                min_val_16_to_31 = bits_16_to_31
            
    return (max_val_2_to_15, min_val_2_to_15), (max_val_16_to_31, min_val_16_to_31)

# Obtener la ruta del directorio actual
current_directory = os.path.dirname(os.path.abspath(__file__))

# Ruta del archivo 'nodosHoja.txt'
input_file_path = os.path.join(current_directory, 'nodosHoja.txt')

# Llamar a la función para extraer y analizar los bits
max_min_2_to_15, max_min_16_to_31 = extract_bits_and_analyze(input_file_path)

# Imprimir resultados
print("Máximo y mínimo en los bits del 2 al 15 (dirección del siguiente árbol):", max_min_2_to_15)
print("Máximo y mínimo en los bits del 16 al 31 (valor de la hoja):", max_min_16_to_31)
