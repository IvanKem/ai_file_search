import random
import re
import os

def calculate_percentage(file_size):
    # Преобразуем размер файла в процент
    # Например, чем меньше размер файла, тем больше процент
    # Можно выбрать любую функцию в зависимости от требований
    # Здесь используем обратную пропорциональность
    return (1 - (1 / file_size))

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
    res = ' '.join(selected_words)
    return res

# Пример использования
file_path = 'test_files/ashy_turing_4268.csv'  # Путь к вашему текстовому файлу

extracted_text = extract_unique_tokens(file_path)
print(extracted_text)