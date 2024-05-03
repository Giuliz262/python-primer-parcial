
def eliminar_duplicados(lista):
    no_duplicados = set()
    resultado = []
    for elemento in lista:
        if elemento not in no_duplicados:
            resultado.append(elemento)
            no_duplicados.add(elemento)
    return resultado

lista_original = [1, 2, 3, 6, 4, 4, 5, 6, 6, 7, 3, 4, 0, 9, 8, 8, 3, 5]
resultado = eliminar_duplicados(lista_original)
print(resultado) 
