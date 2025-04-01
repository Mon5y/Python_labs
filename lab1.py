#task 1
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
b = int(input("enter number:    "))
last_num = 0
for i in range(b,0,-1):
    print(" " * (last_num - i) + "".join(list(map(str, range(1, i + 1)))))
    last_num += len(str(i)) - 1
#task 2.2
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