# Importações
import random
from time import sleep
from lib import ui

# Programa Principal
while True:
    numero = int(input('Quantos números você quer sortear? '))
    if numero < 1:
        print('\033[31mERRO! Digite um valor maior que zero.\033[m')
    else:
        break
while True:
    min = int(input('Qual o menor número? '))
    if min < 0:
        print('\033[31mERRO! Digite um número inteiro maior que zero!\033[m')
    else:
        break
while True:
    max = int(input('Qual o maior número? '))
    if max <= min:
        print('\033[31mERRO! Digite um número inteiro maior que o mínimo.\033[m')
    else:
        break
sorteio = list()
for c in range(numero):
    valor = random.randint(min, max)
    if valor not in sorteio:
        sorteio.append(valor)
print('Os números sorteados foram:', end=' ')
ui.resultado(sorteio, fim=' ', linhas=False)
sleep(2)