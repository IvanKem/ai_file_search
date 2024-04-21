import os
import time

def scan_directory(directory):
    """
    Сканирует указанный каталог и все его вложенные папки, возвращает список файлов и их метаданных, игнорируя файл
    ы и каталоги, начинающиеся с точки.
    """
    files = {}
    for root, dirs, filenames in os.walk(directory):
        # Игнорируем каталоги, начинающиеся с точки
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        for filename in filenames:
            if not filename.startswith('.'):
                filepath = os.path.join(root, filename)
                try:
                    stat = os.stat(filepath)
                    files[filepath] = (stat.st_mtime, stat.st_size)  # Запоминаем время последнего изменения и размер файла
                except FileNotFoundError:
                    # Игнорируем файлы, которые были удалены или переименованы после начала сканирования
                    pass
    return files


def check_changes(previous_state, directory):
    """
    Проверяет изменения в файловой системе сравнивая текущее состояние с предыдущим.
    """
    current_state = scan_directory(directory)

    # Сравниваем текущее состояние с предыдущим
    for filepath, (mtime, size) in current_state.items():
        if filepath not in previous_state:
            print("New file:", filepath)
            # Обработка нового файла
        else:
            prev_mtime, prev_size = previous_state[filepath]
            if prev_mtime != mtime:
                print("Modified file:", filepath)
                # Обработка измененного файла
            elif prev_size != size:
                print("File size changed:", filepath)
                # Обработка измененного размера файла

    # Проверяем удаленные файлы
    for filepath in previous_state:
        if filepath not in current_state:
            print("File deleted:", filepath)
            # Обработка удаленного файла

    return current_state


def main():
    directory = '/home/iv.kem'
    previous_state = scan_directory(directory)

    while True:
        print("Checking for changes...")
        previous_state = check_changes(previous_state, directory)
        time.sleep(10)  # Периодическая проверка каждую минуту


if __name__ == '__main__':
    main()
