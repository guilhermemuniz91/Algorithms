def is_anagram(first_string, second_string):
    """
    Função para verificar se duas strings são anagramas.

    Args:
        first_string: A primeira string a ser comparada.
        second_string: A segunda string a ser comparada.

    Returns:
        Uma tupla contendo a primeira string ordenada,
        a segunda string ordenada e um booleano,
        True se as strings forem anagramas, False caso contrário.
    """

    # Ordena as strings convertidas para minúsculas
    ordered_first_string = quick_sort(
        list(first_string.lower()), 0, len(first_string) - 1
    )
    ordered_second_string = quick_sort(
        list(second_string.lower()), 0, len(second_string) - 1
    )

    joined_first_string = "".join(ordered_first_string)
    joined_second_string = "".join(ordered_second_string)

    # Verifica se as strings ordenadas são iguais.
    if not first_string or not second_string:
        return (joined_first_string, joined_second_string, False)
    else:
        compare_strings = joined_first_string == joined_second_string
        return (joined_first_string, joined_second_string, compare_strings)


def quick_sort(string, start, end):
    if start < end:
        p = partition(string, start, end)
        # Os menores em relação ao pivô ficarão à esquerda
        quick_sort(string, start, p - 1)
        # Os maiores elementos em relação ao pivô ficarão à direita
        quick_sort(string, p + 1, end)
    return string


def partition(string, start, end):
    """
    função auxiliar responsável pela partição do array escolhendo um pivô e
    fazendo movimentações dos sub arrays gerados
    """
    pivot = string[end]
    delimiter = start - 1

    for index in range(start, end):
        # o índice será o elemento em análise no momento,
        # ele passará por todos os elementos
        if string[index] <= pivot:
            delimiter = delimiter + 1
            string[index], string[delimiter] = (
                string[delimiter],
                string[index],
            )

    string[delimiter + 1], string[end] = string[end], string[delimiter + 1]

    return delimiter + 1


"""
o merge_sort tem uma complexidade de tempo de O(n log n) e
poderia ser usado como nossa solução
"""
# def merge_sort(string, start=0, end=None):
#     if end is None:
#         end = len(string)
#     if (end - start) > 1:  # se a lista tiver mais de um elemento, continua
#         mid = (start + end) // 2  # encontrando o meio
#         merge_sort(string, start, mid)  # dividindo as listas
#         merge_sort(string, mid, end)
#         merge(string, start, mid, end)  # unindo as listas
#     return string


# def merge(string, start, mid, end):
#     """Função auxiliar que realiza a mistura dos dois arrays"""
#     left = string[start:mid]  # indexando a lista da esquerda
#     right = string[mid:end]  # indexando a lista da direita

#     left_index, right_index = 0, 0  # as duas listas começarão do início

#     for general_index in range(
#         start, end
#     ):  # percorrer sobre a lista inteira como se fosse uma
#         if left_index >= len(
#             left
#         ):  # se os elementos da esquerda acabaram,
#             # preenche o restante com a lista da direita
#             string[general_index] = right[right_index]
#             right_index = right_index + 1
#         elif right_index >= len(
#             right
#         ):  # se os elementos da direita acabaram,
#             # preenche o restante com a lista da esquerda
#             string[general_index] = left[left_index]
#             left_index = left_index + 1
#         elif (
#             left[left_index] < right[right_index]
#         ):  # se o elemento do topo da esquerda for menor que o da direita,
#             # ele será o escolhido
#             string[general_index] = left[left_index]
#             left_index = left_index + 1
#         else:
#             string[general_index] = right[
#                 right_index
#             ]  # caso o da direita seja menor, ele será o escolhido
#             right_index = right_index + 1


"""
o selection_sort tem uma complexidade de tempo de O(n²) e
nós queremos de no máximo O(n log n)
"""
# def selection_sort(numbers):
#     n = len(numbers)

#     # Início da iteração para ordenar os N-1 elementos
#     for index in range(n - 1):
#         min_element_index = search(numbers, index, n)
#         # Trocando os elementos utilizando desempacotamento.
#         numbers[index], numbers[min_element_index] = (
#             numbers[min_element_index],
#             numbers[index],
#         )

#     return numbers


# def search(numbers, start, end):
#     """
#     função auxiliar para o selection sort
#     """
#     min_element = numbers[start]
#     min_element_index = start

#     for i in range(start + 1, end):  # Busca pelo menor elemento
#         if numbers[i] < min_element:
#             min_element = numbers[i]
#             min_element_index = i

#     return min_element_index  # Retorna a posição do menor elemento


"""
o insertion_sort tem uma complexidade de tempo de O(n²) e
nós queremos de no máximo O(n log n)
"""
# def insertion_sort(numbers):
#     n = len(numbers)  # Quantidade de elementos na lista

#     for index in range(1, n):  # Começaremos a ordenar pelo segundo elemento
#         # Pegamos o segundo elemento e o definimos como chave
#         key = numbers[index]

#         # Tomamos a posição anterior para iniciar a comparação
#         new_position = index - 1
#         # Enquanto a chave for menor, remaneja o elemento para frente
#         while new_position >= 0 and numbers[new_position] > key:
#             # Remaneja o elemento
#             numbers[new_position + 1] = numbers[new_position]
#             new_position = new_position - 1

#         numbers[new_position + 1] = key  # Insere a chave na posição correta

#     return numbers


"""
o bubble_sort tem uma complexidade de tempo de O(n²) e
nós queremos de no máximo O(n log n)
"""
# def bubble_sort(numbers):
#     n = len(numbers)  # Quantidade de elementos na lista

#     for ordered_elements in range(n - 1):  # Precisamos ordenar n-1 elementos
#         for item in range(
#             0, n - 1 - ordered_elements
#         ):  # Vamos percorrer até o elemento anterior ao ordenado
#             if (
#                 numbers[item] > numbers[item + 1]
#             ):  # se um elemento for maior, flutuamos ele para cima
#                 current_element = numbers[item]
#                 numbers[item] = numbers[item + 1]
#                 numbers[item + 1] = current_element

#                 # Lembra da troca com desempacotamento?
#                 numbers[item], numbers[item + 1] = (
#                     numbers[item + 1],
#                     numbers[item],
#                 )
#     return numbers
