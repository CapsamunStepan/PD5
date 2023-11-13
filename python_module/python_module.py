import time
import os
import csv


def function_time(func):
    """
    Декоратор для измерения времени выполнения функции.

    Args:
        func (callable): Функция, время выполнения которой измеряется.

    Returns:
        callable: Обертка вокруг переданной функции.
    """

    def wrapper(*args, **kwargs):
        """
        Обертка вокруг функции, измеряющая время выполнения.

        Returns:
            Any: Результат выполнения оригинальной функции.
        """
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'Время выполнения функции {func.__name__}: {end - start:.4f} сек')
        return result

    return wrapper


def create_directory(directory_path: str):
    """
    Создание директории, если её не существует.

    Args:
        directory_path (str): Путь к директории.
    """
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
        print(f"Директория {directory_path} создана.")
    else:
        print(f"Директория {directory_path} уже существует.")


def create_csv(file_path, header, data):
    """
    Создание файла CSV и запись данных.

    Args:
        file_path: Путь к файлу CSV.
        header: Заголовки столбцов.
        data: Двумерный список данных для записи.
    """
    with open(file_path, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(header)
        csv_writer.writerows(data)

    print(f"Файл CSV создан по пути {file_path}.")


def read_csv(file_path: str):
    """
    Чтение данных из файла CSV.

    Args:
        file_path: Путь к файлу CSV.

    Returns:
        List: Список, содержащий строки из файла CSV.
    """
    data_list = []
    with open(file_path, 'r', newline='') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            data_list.append(row)
    return data_list
