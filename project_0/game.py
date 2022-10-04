"""Игра угадай число
Компьютер сам загадывает и сам угадывает число

"""

import numpy as np

def random_predict(number:int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
        
    """
    
    count = 0
    
    left = 1
    right = 100
    
    while True:
        count += 1
        
        predict_number = (left + right) // 2

        if number == predict_number:
            # Выход из цикла, если угадали
            break 
        else:
            if number < predict_number:
                right = predict_number - 1
            else:
                left = predict_number + 1

    return(count)


def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов 
       угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
        
    """
    # Список для сохранения количества попыток
    count_ls = []  
    # Фиксируем сид для воспроизводимости
    np.random.seed(1)  
    # Загадали список чисел
    random_array = np.random.randint(1, 101, size=(1000))  

    for number in random_array:
        count_ls.append(random_predict(number))
        
    # Находим среднее количество попыток
    score = int(np.mean(count_ls))  

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)


# RUN
if __name__ == '__main__':
    score_game(random_predict)
