import numpy as np

def game_core_v3(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    # Ваш код начинается здесь

    count = 0
    predict = np.random.randint(1, 101)

    if number > 75:
        predict = 76
    elif number > 50:
        predict = 76
    elif number > 25:
        predict = 25
    else:
        predict = 1

    while number != predict:
        count += 1
        if number > predict:
            predict += 1
        elif number < predict:
            predict -= 1

    return count