# Importações
from lib import ui

# Função Principal
while True:
    opções = [
        'Sair',
        'Sorteio de Números',
        'Gerador de Nomes'
    ]
    ui.menu(opções, 'Sorteio')
    resposta = int(input('Escolha: '))
    if resposta == 0:
        ui.cabeçalho('Saindo... Volte Sempre!')
        break

    elif resposta == 1:
        from lib import random_numbers

    elif resposta == 2:
        from lib import random_names

    else:
        print('\033[0;31mERRO! Digite uma opção válida.\033[m')
