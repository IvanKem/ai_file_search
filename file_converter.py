import random
import re
import os
from math import log, ceil


def split_list(lst, n):
    # Вычисляем размер каждой части
    size = len(lst) // n
    # Создаем пустой список для хранения частей
    result = []
    # Разделяем список на n равных частей
    for i in range(0, len(lst), size):
        result.append(','.join(map(str, lst[i:i+size])))
    return result


def calculate_percentage(file_size):
    # Преобразуем размер файла в процент
    # Например, чем меньше размер файла, тем больше процент
    # Можно выбрать любую функцию в зависимости от требований
    # Здесь используем обратную пропорциональность
    print("Объем:" , 1-(log(file_size)/file_size**2))     #(1 - (1 / file_size))
    return (1-(log(file_size)/file_size**2))

def extract_unique_tokens(file_path):
    # Читаем содержимое файла
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Находим все уникальные слова в тексте

    unique_tokens = set()
    with open(file_path, 'r') as file:
        for line in file:
            tokens = line.split()
            unique_tokens.update(tokens)

    # Вычисляем процент на основе размера файла
    file_size = os.path.getsize(file_path)
    percentage = calculate_percentage(file_size)
    unique_tokens = list(unique_tokens)
    # Выбираем случайные слова из множества уникальных слов
    selected_words = random.sample(unique_tokens, int(len(unique_tokens) * percentage))

    res = split_list(selected_words, ceil(log(len(selected_words)))+1) # нормальные значения давало при len=29 split по 5
    return res
'''
# Пример использования
file_path = 'test_files/ashy_turing_4268.res'  # Путь к вашему текстовому файлу

extracted_text = extract_unique_tokens(file_path)
print(extracted_text)
'''
