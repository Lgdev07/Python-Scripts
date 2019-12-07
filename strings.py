frase1 = "Maior que a tristeza de não haver vencido é a vergonha de não ter lutado!"

find_method = frase1.find("vencido")

print(frase1[find_method:]) #vencido é a vergonha de não ter lutado!


# Método que separa string por valor colocado como parâmetro
frase2 = "É melhor conquistar a si mesmo do que vencer mil batalhas."

split_method = frase2.split('a')

print(split_method) #['É melhor conquist', 'r ', ' si mesmo do que vencer mil b', 't', 'lh', 's.']