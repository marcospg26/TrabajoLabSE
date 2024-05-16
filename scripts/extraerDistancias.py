import os

def hex_to_bin(hex_str):
    return bin(int(hex_str, 16))[2:].zfill(32)

def calculate_relative_distance(current_addr, next_addr_bin):
    current_addr_int = int(current_addr, 2)
    next_addr_int = int(next_addr_bin, 2)
    return next_addr_int - current_addr_int

def analyze_relative_distances(input_file, output_file):
    with open(input_file, 'r') as f_in:
        lines = f_in.readlines()

    distances = []
    
    with open(output_file, 'w') as f_out:
        for line in lines:
            address, leaf_node = line.strip().split(':')
            leaf_node_bin = hex_to_bin(leaf_node)
            next_addr_bin = leaf_node_bin[2:15]  # Extrae los bits del 2 al 14 (incluidos)
            distance = calculate_relative_distance(address, next_addr_bin)
            distances.append(distance)
            f_out.write(f"{address}:{leaf_node}:{distance}\n")
    
    # Calcula la distancia mínima y máxima
    min_distance = min(distances)
    max_distance = max(distances)
    
    # Muestra el rango de distancias
    print(f"Distancia mínima: {min_distance}")
    print(f"Distancia máxima: {max_distance}")

# Obtener la ruta absoluta del script actual
script_dir = os.path.dirname(os.path.abspath(__file__))

# Ruta del archivo de entrada
input_file_path = os.path.join(script_dir, 'nodosHojaConDirecciones.txt')

# Ruta del archivo de salida
output_file_path = os.path.join(script_dir, 'nodosHojaConDistancias.txt')

# Uso de la función
analyze_relative_distances(input_file_path, output_file_path)
