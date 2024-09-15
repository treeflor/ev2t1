def suma_acumulada(n):
    if n == 1:
        return 1
    else:
        return n + suma_acumulada(n - 1)

# Llamando a la función con el número 20
resultado = suma_acumulada(20)
print(resultado)  # Esto imprimirá 210