# Print
print("Hello World!")

# Operadores
5 + 2

3.9 > 4

# Tipos
type("abcd")
type(1)
type(2.3)
type(False)
type(None)

# Arrays
x = 2
x = [1, 2.5, "3.89", False, [1, 2], None]

x[0]
x[1]

# -1 é o ultimo elemento
# -2 é p penultimo
# e assim sucessivamente
x[-1]

# Notacao Slice
# Primeiro elemento inclusivo (Inclui o indice), segundo parameto exclusivo(Exclui o elemento)
x[0:3]

# Inicia no indice 1 e busque até o quarto elemento
x[1:4]

# pega os tres primeiros
x[:3]
x[0:3]

# Tres ultimos elementos
x[-3:]
x[-3:-1]

# Pega os indices pares
x[::2]

# Pega os indices impares
x[1::2]

# Inverte a lista
x[::-1]


# Definindo uma função
def soma2(a, b=2):
    return a + b


soma2(6)
soma2(2, 1)


# fibonacci

def fibo(n):
    if n < 1:
        print("O valor de n deve ser > 1")
        return
    elif n == 1 or n == 2:
        return 1

    else:
        return fibo(n - 1) + fibo(n - 2)

fibo(10)