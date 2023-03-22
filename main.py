import random

print ('Welcome to Password Generator')

#definindo uma string com todos os valores possiveis
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%¨&*().,?/|\{}[]'

number = input('Number of passwords to be generated: ') #variavel para armazenar o numero de senhas que serao geradas
number = int(number) #fixando a variavel como int

lenght = input("Number of characters: ")#variavel para armazenar o numero de caracteres das senhas
lenght = int(lenght)

print ('\nhere are your passwords:')

for i in range (number):
    passwords = '' #definindo uma string vazia dentro do loop
    for j in range (lenght):
        passwords += random.choice(chars) #preenchendo a string com valores aleatorios vindos da string chars
    print(passwords)

