import time
import unittest
from python_module.python_module import function_time, create_directory, create_csv, read_csv
import os


class TestCommonUtils(unittest.TestCase):

    def test_function_time(self):
        # Тестирование декоратора function_time
        @function_time
        def dummy_function():
            time.sleep(1)
            pass

        result = dummy_function()
        self.assertEqual(result, 'Время выполнения функции dummy_function: 1.0 сек')

    def test_create_directory(self):
        # Тестирование функции create_directory
        test_dir = 'test_directory'

        # Проверка успешного создания директории
        create_directory(test_dir)
        self.assertTrue(os.path.exists(test_dir))

    def test_create_and_read_csv(self):
        # Тестирование функций create_csv и read_csv
        test_file = 'test_csv.csv'
        header = ['Name', 'Age', 'City']
        data = [['John', '25', 'New York'], ['Alice', '30', 'Los Angeles']]

        # Проверка успешного создания и чтения CSV-файла
        create_csv(test_file, header, data)
        read_data = read_csv(test_file)
        read_data = read_data[1:]
        self.assertEqual(read_data, data)

        # Очистка созданных файлов
        os.remove(test_file)


if __name__ == '__main__':
    unittest.main()
