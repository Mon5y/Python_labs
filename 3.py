#task 0
print("task 0")
numbers = [int(x) for x in input("Введите числа через пробел: ").split()]
result = [numbers[i] for i in range(1, len(numbers)) if numbers[i] > numbers[i-1]]
print(result)

#task 1
print("task 1")
num = [int(x) for x in input("Введите элементы списка: ").split()]
m_ax = max(num)
m_in = min(num)
index_max = num.index(m_ax)
index_min = num.index(m_in)
num[index_max], num[index_min] = num[index_min], num[index_max]
print("Список после замены местами максимального и минимального чисел:", num)

#task 2
print("task 2")
list_1 = [int(x) for x in input("Введите числа через пробел: ").split()]
list_2 = [int(x) for x in input("Введите числа через пробел: ").split()]

element = set(list_1) & set(list_2)
coutn = len(element)
print("количество общих симвлов:    " , coutn)
#atsk 3
print("task 3")

def count_string_repetitions(string_list):
    count_dict = {}
    
    for string in string_list:
        if string in count_dict:
            count_dict[string] += 1
        else:
            count_dict[string] = 1
            
    return list(count_dict.values())

# Примеры входных данных
input_data1 = ['abc', 'bcd', 'abc', 'abd', 'abd', 'dcd', 'abc']
input_data2 = ['aaa', 'bbb', 'ccc']
input_data3 = ['abc', 'abc', 'abc']

# Вывод результатов
print("Первый список:", count_string_repetitions(input_data1))
print("Второй список:", count_string_repetitions(input_data2))
print("Третий список:", count_string_repetitions(input_data3))            
    
