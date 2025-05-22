#task 1
print("task 1")
n = int(input("enter size:  "))
s = "qwertyuiopasdfghjklzxcvbnm"
val = [(int(input(f"Введите значение {s[i]}: ")), s[i]) for i in range(n)]


for i in range(n-1):
    for j in range(n - i - 1):    
        if val[j][0] > val[j+1][0]:
            val[j], val[j+1] = val[j+1], val[j] 

print(val[0][1], end=" ")
for i in range(1,n):
    print("=<"[int(val[i][0] > val[i - 1][0])] + " " + val[i][1], end=" ")
#task 2.1
print("task 2.1")
b = int(input("enter number:    "))
last_num = 0
for i in range(b,0,-1):
    print(" " * (last_num - i) + "".join(list(map(str, range(1, i + 1)))))
    last_num += len(str(i)) - 1
#task 2.2
print("task 2.2")
def rev_pyramid(x):
    for i in range(x,0,-1):
        space = " "*(x - i)
        line = ""
        for j in range(1,i+1):
            line +=str(j)
        for j in range(i-1,0,-1):
            line +=str(j)
        print(space + line)
x = int(input("enter size pyramid:  "))
rev_pyramid(x)
# task 3
print("task 3")
def pascal_triangle(n):
    triangle = []
    for i in range(n):
        row = [1]*(i+1)
        for j in range(1,i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        triangle.append(row)
    return triangle
def end_element(triangle):
    max_len = 0
    for row in triangle:
        for num in row:
            current_len = len(str(num))
            max_len = max(max_len,current_len)
    return max_len
def print_pascal_triangle(triangle):
    max_len = end_element(triangle)
    max_width = len(' '.join(str(num).ljust(max_len) for num in triangle[-1]))
    for row in triangle:
        row_str = ' '.join(str(num).ljust(max_len) for num in row)
        print(row_str.center(max_width))

n = int(input("enter size:  "))
pascals_triangle = pascal_triangle(n)
print("\nтреугольник паскаля:   ")
print_pascal_triangle(pascals_triangle)
