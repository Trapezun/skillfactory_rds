"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


#реализация игры.
#Основная идея в том, чтобы разбить диапазон чисел на две равные части и искать число только в одной из частей.
#И так делаем рекурсивно, пока не найдем число
def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    

    #Класс для хранения счетчика. Его передаю в ф-ии угадывания
    class gameData:    
        counter=0

    #Функция, которая угадывает число.
    def _guess(minValue, maxValue, data):         
        #увеличиваю счетчик
        data.counter += 1

        #если входные значения равны заданному числу, то выхожу.
        if minValue == number:              
            return
        elif maxValue == number:        
            return                   
        
        #беру середину между maxValue и minValue
        middle = ((maxValue - minValue) / 2)
        middle = np.round(middle)

        #делаю 2 новых дипазона.
        #с минимального до середины и с середины до максимального
        from1 = minValue
        to1 = minValue + middle;

        from2 = to1;
        to2 = maxValue;
    
        #в зависимости в какой дипазано попало число, снова вызываю ф-ю угадывания.
        if (number >= from1 and number <= to1):            
            _guess(from1, to1, data)    
        else:            
            _guess(from2, to2, data)                  
    
    data = gameData()
    _guess(1, 101, data);
   
    return data.counter;


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))
    
    
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
