# Este script extrae los numeros hexadecimales pares del test (nodos rama) para 
# llevarlos a un archivo de texto.

import os
import re

# Función para extraer números hexadecimales terminados en 0 a nivel de bit
def extract_hex_numbers(input_file, output_file):
    with open(input_file, 'r') as f_in:
        with open(output_file, 'w') as f_out:
            for line in f_in:
                # Busca patrones de la forma 'x"XXXXXX"' en las líneas
                matches = re.findall(r'x"([0-9a-fA-F]+)"', line)
                # Si encuentra una coincidencia, verifica si termina en 
                # 0, 2, 4, 6, 8 o A, C, E a nivel de bit y escribe en el archivo de salida
                if matches:
                    for match in matches:
                        # Verifica si el último dígito es uno de los siguientes: 
                        # 0, 2, 4, 6, 8, A, C o E (pares en binario)
                        if match[-1] in ['0', '2', '4', '6', '8', 'a', 'c', 'e']:
                            f_out.write(match + '\n')  # Escribe el número en el archivo de salida

# Obtener la ruta absoluta del script actual
script_dir = os.path.dirname(os.path.abspath(__file__))

# Ruta del archivo de entrada
input_file_path = os.path.join(script_dir, '..', 'src', 'marcos_test.vhd')

# Ruta del archivo de salida
output_file_path = os.path.join(script_dir, 'nodosRama.txt')

# Uso de la función
extract_hex_numbers(input_file_path, output_file_path)
