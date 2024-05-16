import os
import re

def extract_addresses_and_leaf_nodes(input_file, output_file):
    with open(input_file, 'r') as f_in:
        lines = f_in.readlines()

    with open(output_file, 'w') as f_out:
        for i in range(len(lines)):
            # Busca la línea con la dirección
            address_match = re.match(r'Addr\s*<=\s*"([01]+)";', lines[i].strip())
            if address_match:
                address = address_match.group(1)
                if i + 1 < len(lines):
                    # Busca la línea con el nodo hoja
                    leaf_node_match = re.match(r'Trees_din\s*<=\s*x"([0-9a-fA-F]+)";', lines[i + 1].strip())
                    if leaf_node_match:
                        leaf_node = leaf_node_match.group(1)
                        # Verifica si el nodo hoja termina en un dígito impar
                        if leaf_node[-1].lower() in ['1', '3', '5', '7', '9', 'b', 'd', 'f']:
                            f_out.write(f"{address}:{leaf_node}\n")

# Obtener la ruta absoluta del script actual
script_dir = os.path.dirname(os.path.abspath(__file__))

# Ruta del archivo de entrada
input_file_path = os.path.join(script_dir, 'marcos_test.vhd')

# Ruta del archivo de salida
output_file_path = os.path.join(script_dir, 'nodosHojaConDirecciones.txt')

# Uso de la función
extract_addresses_and_leaf_nodes(input_file_path, output_file_path)
