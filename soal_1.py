def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Contoh penggunaan
n = 5
result = factorial(n)
print(f"Faktorial dari {n} adalah {result}")
