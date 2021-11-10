# Multiplicar sin el simbolo de multiplicación

def multiply(a, b):
    if b == 0:
        return 0
    else:
        return a + multiply(a, b - 1)

resultado = multiply(10, 10)
print(resultado)