n = 3
variable_names = 'abcdefgh'
values = [(int(input(f"Введите значение {variable_names[i]}: ")), variable_names[i]) for i in range(n)]

for i in range(n - 1):
    for j in range(n - 1 - i):
        if values[j][0] > values[j + 1][0]:
            values[j], values[j + 1] = values[j + 1], values[j]
print(values[0][1], end=" ")
for i in range(1, n):
    print("=<"[int(values[i][0] > values[i - 1][0])] + " " + values[i][1], end=" ")
    
