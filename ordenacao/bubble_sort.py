"""Algoritmo de ordenação por bolha (bubble sort):"""
def executar_bubble_sort(lista):
    """Algoritmo de ordenação por bolha (bubble sort):"""
    tamanho = len(lista)
    for i in range(tamanho-1):
        for j in range(tamanho-1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

lista1 = [10, 8, 7, 3, 2, 1]
lista_ordenada = executar_bubble_sort(lista1)
print(lista_ordenada)
