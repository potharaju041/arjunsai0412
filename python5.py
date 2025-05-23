def calculator(a, b, op):
    if op == '+': return a + b
    if op == '-': return a - b
    if op == '*': return a * b
    if op == '/': return a / b
    return "Invalid operator"

print(calculator(10, 5, '+'))  # 15
