import string, random

alphabet = string.ascii_lowercase

vowels = ['a', 'e', 'i', 'o', 'u']

nick = ''

print('Welcome to the nickname generator!!\n')
letters = int(input('Enter the number of letters: '))

while letters > 0:
    nick += random.choice(alphabet)
    letters -= 1
    if letters == 0:
        break
    nick += random.choice(vowels)
    letters -= 1

print(f'\n{nick}\n')
