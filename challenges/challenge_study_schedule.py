def study_schedule(permanence_periods, target_time):
    """
    Função para encontrar o maior número de estudantes no mesmo horário.

    Args:
        permanence_periods: Lista de tuplas representando os períodos de
        tempo de estudo dos estudantes no sistema.

        target_time: Horário para verificar a quantidade de pessoas estudantes
        ativas.

    Returns:
        O horário com a maior quantidade de pessoas estudantes ativas.
    """
    try:
        count = 0
        study_time = permanence_periods[0], permanence_periods[1]
        for study_time in permanence_periods:
            if study_time[0] <= target_time <= study_time[1]:
                count += 1
        return count
    except TypeError:
        return None
