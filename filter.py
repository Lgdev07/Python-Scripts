# Temos uma função.

# Queremos fazer um filtro nela, retornando somente os valores de uma certa condição.

# Por exemplo:

lista = range(-10, 10)

filtro = list(filter(lambda x: x < -5, lista))

print(filtro)

# Python Program to find palindromes in  
# a list of strings. 
  
my_list = ["geeks", "geeg", "keek", "practice", "aa"] 
  
# use anonymous function to filter palindromes. 
# Please refer below article for details of reversed 
# https://www.geeksforgeeks.org/reverse-string-python-5-different-ways/ 
result = list(filter(lambda x: (x == "".join(reversed(x))), my_list))  
  
# printing the result 
print(result)  

string = 'teste'

from collections import Counter 

print(Counter(string))

string = 'grrksfoegrrks'

res = list(filter(lambda x: x == 'r', string))

print(res)