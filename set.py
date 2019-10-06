import time

def procedure1():
    lista = [1,2,3]

    print(lista)

    print(1 in lista)

def procedure2():
    sete = set([1,2,3])

    print(sete)

    print(1 in sete)

t0 = time.time()
procedure1()
print (time.time() - t0, "seconds")

t1 = time.time()
procedure2()
print (time.time() - t1, "seconds")

x = input('What is Software Legacy? ')

print(x)

