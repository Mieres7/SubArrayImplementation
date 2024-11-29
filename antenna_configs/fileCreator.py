def process_text_file(input_file, output_file):
    """
    Procesa un archivo de texto delimitado por comas, selecciona columnas específicas, y genera un archivo .cfg
    con las columnas en el orden especificado, agregando el cálculo de 'diam'.

    :param input_file: Ruta del archivo de entrada (archivo de texto delimitado por comas).
    :param output_file: Ruta del archivo de salida (.cfg).
    """
    try:
        with open(input_file, 'r', encoding='utf-8') as infile:
            lines = infile.readlines()
        
        # Procesar encabezado
        header = lines[0].strip().split(',')
        column_indices = {
            "Dish name": header.index("Label"),
            "ECEF-X": header.index("ECEF-X"),
            "ECEF-Y": header.index("ECEF-Y"),
            "ECEF-Z": header.index("ECEF-Z"),
        }
        
        with open(output_file, 'w', encoding='utf-8') as outfile:
            # Escribir encabezado en el archivo de salida
            outfile.write("ECEF-X ECEF-Y ECEF-Z diam Label\n")
            
            # Procesar cada fila
            for line in lines[1:]:
                values = line.strip().split(',')
                dish_name = values[column_indices["Dish name"]]
                ecef_x = values[column_indices["ECEF-X"]]
                ecef_y = values[column_indices["ECEF-Y"]]
                ecef_z = values[column_indices["ECEF-Z"]]
                
                # Calcular 'diam' según las condiciones
                if dish_name.startswith('M'):
                    diam = 13.5
                elif dish_name.startswith('S'):
                    diam = 15.0
                else:
                    diam = 40.0
                
                # Escribir en el archivo de salida
                outfile.write(f"{ecef_x} {ecef_y} {ecef_z} {diam} {dish_name}\n")
        
        print(f"Archivo .cfg generado exitosamente: {output_file}")
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {input_file}.")
    except Exception as e:
        print(f"Error inesperado: {e}")

# Parámetros
input_file = 'skalowcoords.txt'  # Cambiar por el nombre del archivo de entrada
output_file = 'skalowcoordsNew.cfg'  # Nombre del archivo de salida

# Ejecutar la función
process_text_file(input_file, output_file)
