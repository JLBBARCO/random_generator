# Importações
import random
from time import sleep

def linha(tam=60):
    """
    -> Cria uma linha de separação.
    :param tam: O tamanho da linha. Padrão é 60.
    :return: None
    """
    print('-' * tam)

def cabeçalho(txt):
    """
    -> Cria um cabeçalho para o programa.
    :param txt: O texto a ser exibido no cabeçalho.
    :return: None
    """
    linha()
    print(txt.center(60))
    linha()

def menu(opções=[], título='MENU DE OPÇÕES'):
    """
    -> Cria um menu de opções para o programa.
    :param opções: Informações sobre a opção.
    :param título: Título do menu, se não for passado, o padrão é 'MENU DE OPÇÕES'. False para não mostrar o título.
    """
    if título == False:
        pass
    else:
        cabeçalho(título)
    for i, c in enumerate(opções):
        print(f'\033[33m{i}\033[m - \033[34m{c}\033[m')

def resultado(valor, fim='', linhas=True):
    """
    -> Personaliza o return de algum resultado.
    :param valor: Valor do resultado.
    :param fim: Declara qual vai ser o end do print. Padrão vazio.
    :param linhas: Declara se vai mostrar linhas nas partes de cima e baixo do resultado. Padrão True.
    """
    if isinstance(valor, (list, dict, tuple)):
        if linhas is True:
            linha()
        for c in valor:
            print(c, end=fim)
        print()
    else:
        print(valor, end=fim)

def sorteio_números():
    """
    -> Pede ao usuário a quantidade de números a serem sorteados, o mínimo e o máximo. Enquanto o usuário digita, o programa valida, sendo os critérios: todos os parâmetros tem que ser números inteiros, a quantidade não pode ser menor que 1, o mínimo não pode ser menor que 0, e o máximo não pode ser menor ou igual ao número mínimo. Ao sortear, verifica se o número sorteado já saiu. Se sim, sorteia outro.
    """
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
            print('\033[31mERRO! Digite um número inteiro maior que o mínimo.')
        else:
            break
    sorteio = list()
    for c in range(numero):
        valor = random.randint(min, max)
        if valor not in sorteio:
            sorteio.append(valor)
        else:
            return valor
    print('Os números sorteados foram:', end=' ')
    resultado(sorteio, fim=' ', linhas=False)
    sleep(2)

def gerador_nomes():
    """
    -> Pede ao usuário a quantidade de nomes a serem gerados, e gera uma lista com esses nomes.
    """
    quantidade = int(input('Digite a quantidade de nomes: '))
    nomes = list()
    from faker import Faker
    fake = Faker()
    for _ in range(quantidade):
        nome = fake.name()
        nomes.append(nome)
    resultado(nomes, fim='; ')

# Função Principal
try:
    while True:
        opções = [
            'Sair',
            'Sorteio de Números',
            'Gerador de Nomes'
        ]
        menu(opções, 'Sorteio')
        resposta = int(input('Escolha: '))
        if resposta == 0:
            cabeçalho('Saindo... Volte Sempre!')
            break

        elif resposta == 1:
            sorteio_números()

        elif resposta == 2:
            gerador_nomes()
            
        else:
            print('\033[0;31mERRO! Digite uma opção válida.\033[m')
except resposta is float or str:
    print('\033[31mERRO! Digite um número inteiro válido.\033[m')
