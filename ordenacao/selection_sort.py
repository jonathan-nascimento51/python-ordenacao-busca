"""Algoritmo de ordenação por seleção (selection sort):"""
def executar_selection_sort(lista):
    """Algoritmo de ordenação por seleção (selection sort):"""
    tamanho = len(lista)
    for i in range(0, tamanho-1):
        minimo = i
        for j in range(i+1, tamanho):
            if lista[j] < lista[minimo]:
                minimo = j
        lista[i], lista[minimo] = lista[minimo], lista[i]
    return lista

lista1 = [10, 8, 7, 3, 2, 1]
lista_ordenada = executar_selection_sort(lista1)
print(lista_ordenada)
