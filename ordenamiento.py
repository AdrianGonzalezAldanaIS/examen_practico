def ordena_lista_pythonica(lista: list) -> list:
    if len(lista) == 0:
        print("Lista vacia")
        return []
    
    lista_ordenada = sorted(lista)
    return lista_ordenada

def ordena_lista_no_pythonica(lista: list) -> list:
    max_value = -float('inf')
    min_value = float('inf')
    
    if len(lista) == 0:
        return []
    
    lista_ordenada = []
    lista_copy = lista[:]

    while len(lista_copy) > 0:
        for num in lista_copy:
            if num < min_value:
                min_value = num
            if num > max_value:
                max_value = num
        
        lista_ordenada.append(min_value)
        lista_copy.remove(min_value)
        
        min_value = float('inf')

    return lista_ordenada



lista = [29, 10, 14, 37, 13, 5, 78, 2, 56, 45]
lista_ordenada = ordena_lista_pythonica(lista)
print("Lista ordenada pythónicamente:", lista_ordenada)
     
lista_ordenada = ordena_lista_no_pythonica(lista)
print("Lista ordenada no pythónicamente:", lista_ordenada)



