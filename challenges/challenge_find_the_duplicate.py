def find_duplicate(nums):
    """Função para encontrar os números que se repetem da lista."""

    unique_numbers = set()
    for num in nums:
        if type(num) is not int or num < 0:
            return False

        if num in unique_numbers:
            return num
        else:
            unique_numbers.add(num)

    return False
