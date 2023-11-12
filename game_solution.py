import numpy as np


def game_core_v3(number: int = 1) -> int:
    """Алгоритм угадывает число от 1 до 100. 1 и 100 занесены
    в отдельную переменную, чтобы можно было менять диапазон
    угадывания (увеличивать минимальное значение и уменьшать максимальное)
    в ходе угадывания
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """

    count, low, high = 0, 1, 101

    while True:
        if low == high:
            predict_numb = low
            break
        count += 1
        predict_numb = np.random.randint(low, high)

        if number != predict_numb:
            if predict_numb < number:
                low = predict_numb + 1
            else:
                high = predict_numb - 1
        else:
            break
    return count
