import numpy as np

def game_core_v3(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    # Ваш код начинается здесь

    count = 1
    predict = np.random.randint(1, 101)

    if number > 85:
        predict = 86
    elif number > 70:
        predict = 71
    elif number > 65:
        predict = 66
    elif number > 50:
        predict = 51       
    elif number > 35:
        predict = 36     
    elif number > 20:
        predict = 21 
    elif number > 5:
        predict = 6
    else:
        predict = 1

    while number != predict:
        count += 1
        if number > predict:
            predict += 1
        elif number < predict:
            predict -= 1

    return count