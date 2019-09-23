# Lambda é como se fosse uma mini função

def soma_func(x, y):
    return x + y

soma_lambda = lambda x, y: x + y

print(soma_func(1, 1))

print(soma_lambda(2, 4))

maior_que_10 = lambda x: x > 10

print(maior_que_10)