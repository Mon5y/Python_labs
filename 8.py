import csv
import os
import random

class CSVHandler:
    def __init__(self, filename, delimiter=','):
        self.filename = filename
        self.delimiter = delimiter
        self.headers = []
        self.data = []
        self._load_file()
    
    def _load_file(self):
        with open(self.filename, 'r', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=self.delimiter)
            self.headers = next(reader)
            self.data = [row for row in reader]
    
    def Show(self, mode='top', n=5, separator=','):
        total_rows = len(self.data)
        if total_rows < n:
            print(f"Строк недостаточно: всего {total_rows}, запрошено {n}. Вывод всех строк.")
            n = total_rows
        
        if mode == 'top':
            rows = self.data[:n]
        elif mode == 'bottom':
            rows = self.data[-n:]
        elif mode == 'random':
            rows = random.sample(self.data, n)
        else:
            print("Недопустимый режим. Используется 'top'.")
            rows = self.data[:n]
        
        # Вывод заголовков
        header_line = separator.join(self.headers)
        print(header_line)
        print('-' * len(header_line))
        
        # Вывод данных
        for row in rows:
            print(separator.join(row))
    
    def Info(self):
        num_rows = len(self.data)
        num_cols = len(self.headers)
        print(f"Размер данных: {num_rows} строк x {num_cols} столбцов")
        
        # Сбор статистики по столбцам
        for col_idx, col_name in enumerate(self.headers):
            non_empty_count = 0
            col_types = set()
            
            for row in self.data:
                cell = row[col_idx].strip()
                if cell:
                    non_empty_count += 1
                    # Определение типа данных
                    try:
                        int(cell)
                        col_types.add(int)
                    except:
                        try:
                            float(cell)
                            col_types.add(float)
                        except:
                            col_types.add(str)
            
            # Определение итогового типа столбца
            if str in col_types:
                col_type = 'string'
            elif float in col_types:
                col_type = 'float'
            elif int in col_types:
                col_type = 'int'
            else:
                col_type = 'string'  # Если все пустые
            
            print(f"{col_name:<15} {non_empty_count:<5} {col_type}")
    
    def DelNaN(self):
        self.data = [
            row for row in self.data
            if all(cell.strip() for cell in row)
        ]
    
    def MakeDS(self):
        # Перемешиваем данные
        random.shuffle(self.data)
        split_idx = int(0.7 * len(self.data))
        train_data = self.data[:split_idx]
        test_data = self.data[split_idx:]
        
        # Создание директорий
        base_dir = 'workdata'
        learning_dir = os.path.join(base_dir, 'Learning')
        testing_dir = os.path.join(base_dir, 'Testing')
        os.makedirs(learning_dir, exist_ok=True)
        os.makedirs(testing_dir, exist_ok=True)
        
        # Запись данных
        def write_csv(path, data):
            with open(path, 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file, delimiter=self.delimiter)
                writer.writerow(self.headers)
                writer.writerows(data)
        
        write_csv(os.path.join(learning_dir, 'train.csv'), train_data)
        write_csv(os.path.join(testing_dir, 'test.csv'), test_data)
        print(f"Данные разделены: {len(train_data)} строк -> Learning/train.csv, {len(test_data)} строк -> Testing/test.csv")

# Пример использования
if __name__ == "__main__":
    # Инициализация обработчика (указать путь к файлу)
    handler = CSVHandler('your_file.csv')  # Замените на имя вашего файла
    
    # Демонстрация функций
    print("--- Show() ---")
    handler.Show(mode='top', n=3)
    
    print("\n--- Info() ---")
    handler.Info()
    
    print("\n--- DelNaN() ---")
    handler.DelNaN()
    handler.Info()
    
    print("\n--- MakeDS() ---")
    handler.MakeDS()