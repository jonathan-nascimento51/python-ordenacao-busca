"""Algoritmo de ordenação merge sort"""
def executar_merge_sort(lista):
    """Algoritmo de ordenação merge sort"""
    if len(lista) <= 1:
        return lista
    else:
        meio = len(lista) // 2
        esquerda = executar_merge_sort(lista[:meio])
        direita = executar_merge_sort(lista[meio:])
        return executar_merge(esquerda, direita)

def executar_merge(esquerda, direita):
    """Algoritmo de ordenação merge sort"""
    sub_lista_ordenada = []
    topo_esquerda, topo_direita = 0, 0
    while topo_esquerda < len(esquerda) and topo_direita < len(direita):
        if esquerda[topo_esquerda] <= direita[topo_direita]:
            sub_lista_ordenada.append(esquerda[topo_esquerda])
            topo_esquerda += 1
        else:
            sub_lista_ordenada.append(direita[topo_direita])
            topo_direita += 1
    sub_lista_ordenada += esquerda[topo_esquerda:]
    sub_lista_ordenada += direita[topo_direita:]
    return sub_lista_ordenada

lista1 = [10, 8, 7, 8, 3, 2, 1]
lista_ordenada = executar_merge_sort(lista1)
print(lista_ordenada)
