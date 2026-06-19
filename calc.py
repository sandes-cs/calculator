def add(a, b): return a + b
def subtract(a, b): return a - b  
def multiply(a, b): return a * b
def divide(a, b): return "Error" if b == 0 else a / b

print("Sandes Calculator")
x = float(input("First number: "))
y = float(input("Second number: "))
op = input("Operation + - * / : ")

if op == '+': print(add(x, y))
elif op == '-': print(subtract(x, y))
elif op == '*': print(multiply(x, y))
elif op == '/': print(divide(x, y))
else: print("Invalid")
