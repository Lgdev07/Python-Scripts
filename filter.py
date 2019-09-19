# Temos uma função.

# Queremos fazer um filtro nela, retornando somente os valores de uma certa condição.

# Por exemplo:

lista = range(-10, 10)

filtro = list(filter(lambda x: x < -5, lista))

print(filtro)
