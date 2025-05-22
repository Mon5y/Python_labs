#task 1
print("task 1")
s = input("Введите строку: ")
counts = {}
for ch in s:
    counts[ch] = counts.get(ch, 0) + 1
result = []
for ch in counts:
    result.append(ch + str(counts[ch]))
print(''.join(result))
#task 1.1
s = input("Введите строку (например, h1e1l2o1): ")
result = []

i = 0
while i < len(s):
    ch = s[i]
    i += 1
    count = 0

    while i < len(s) and s[i].isdigit():
        count = count * 10 + int(s[i])
        i += 1

    result.append(ch * count)

print(''.join(result))
#task 2
print("task 2")
from collections import Counter

s = input("Введите строку: ")


counts = Counter(s)


most_common = counts.most_common(3)


for ch, count in most_common:
    print(f"Символ: '{ch}' встречается {count} раз(а).")

#task 3
print("task 3")
def number_to_words(n):
    units = [
        "", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять",
        "десять", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать",
        "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать"
    ]
    
    tens = [
        "", "", "двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", 
        "семьдесят", "восемьдесят", "девяносто"
    ]
    
    hundreds = [
        "", "сто", "двести", "триста", "четыреста", "пятьсот", "шестьсот", 
        "семьсот", "восемьсот", "девятьсот"
    ]
    
    if n < 1 or n > 1000:
        return "Число должно быть в диапазоне от 1 до 1000."

    if n == 1000:
        return "тысяча"

    word = ""
    
    if n >= 100:
        word += hundreds[n // 100] + " "
        n %= 100
    
    if n >= 20:
        word += tens[n // 10] + " "
        n %= 10
    
    if n > 0:
        word += units[n] + " "
    
    return word.strip()

# Ввод числа от пользователя
try:
    number = int(input("Введите число от 1 до 1000: "))
    print(number_to_words(number))
except ValueError:
    print("Пожалуйста, введите корректное целое число.")