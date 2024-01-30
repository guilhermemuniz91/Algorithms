def is_palindrome_iterative(word):
    """Função para verificar se uma palavra é um palíndromo."""
    if len(word) == 0:
        return False

    # solução com slicing
    if word != word[::-1]:
        return False
    return True

    # solução com range
    # for i in range(len(word)):
    #     if word[i] != word[len(word) - 1 - i]:
    #         return False
    # return True
