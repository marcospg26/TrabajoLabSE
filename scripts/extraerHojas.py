# Este script extrae los numeros hexadecimales impares del test (nodos hoja) 
# para  llevarlos a un archivo de texto.

import os
import re

# Función para extraer números hexadecimales terminados en número impar a nivel de bit
def extract_hex_numbers(input_file, output_file):
    with open(input_file, 'r') as f_in:
        with open(output_file, 'w') as f_out:
            for line in f_in:
                # Busca patrones de la forma 'x"XXXXXX"' en las líneas
                matches = re.findall(r'x"([0-9a-fA-F]+)"', line)
                # Si encuentra una coincidencia, verifica si termina en número impar
                if matches:
                    for match in matches:
                        # Verifica si el último dígito es uno de los siguientes: 
                        # 1, 3, 5, 7, 9, B, D o F (impares en binario)
                        if match[-1] in ['1', '3', '5', '7', '9', 'b', 'd', 'f']:
                            f_out.write(match + '\n')  # Escribe el número en el archivo de salida

# Obtener la ruta absoluta del script actual
script_dir = os.path.dirname(os.path.abspath(__file__))

# Ruta del archivo de entrada
input_file_path = os.path.join(script_dir, '..', 'src', 'marcos_test.vhd')

# Ruta del archivo de salida
output_file_path = os.path.join(script_dir, 'nodosHoja.txt')

# Uso de la función
extract_hex_numbers(input_file_path, output_file_path)
