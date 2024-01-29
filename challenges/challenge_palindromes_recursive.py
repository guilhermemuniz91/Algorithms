def is_palindrome_recursive(word, low_index, high_index):
    """
    Função recursiva para verificar se uma palavra é um palíndromo.

    Args:
        word: A palavra a ser verificada.
        low_index: O índice inicial da palavra.
        high_index: O índice final da palavra.

    Returns:
        True se a palavra for um palíndromo, False caso contrário.
    """
    if len(word) == 0:
        return False
    if low_index >= high_index:
        return True
    if word[low_index] != word[high_index]:
        return False
    return is_palindrome_recursive(word, low_index + 1, high_index - 1)
