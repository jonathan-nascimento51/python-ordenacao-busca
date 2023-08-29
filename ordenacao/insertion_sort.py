"""Selection sort: (Classificação por inserção)"""
def executar_insertion_sort(lista):
    """Selection sort: (Classificação por inserção)"""
    tamanho = len(lista)
    for i in range(1, tamanho):
        valor_inserir = lista[i]
        j = i - 1

        while j >= 0 and lista[j] > valor_inserir:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = valor_inserir

    return lista

lista1 = [10, 8, 7, 3, 2, 1]
lista_ordenada = executar_insertion_sort(lista1)
print(lista_ordenada)
