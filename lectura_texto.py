
def contar_palabras(archivo):
    palabras= None
    cantidad_palabras = None
    try:
        with open(archivo, 'r', encoding='utf-8') as file:
            contenido = file.read()

            palabras = contenido.split()

            cantidad_palabras = len(palabras)
            
            return cantidad_palabras
    except FileNotFoundError:
        print(f"El archivo {archivo} no se encontró.")
        return 0


nombre_archivo = 'texto1.txt'
total_palabras = contar_palabras(nombre_archivo)
print(f"El archivo {nombre_archivo} contiene {total_palabras} palabras.")
