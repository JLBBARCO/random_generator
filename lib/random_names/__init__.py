# Importações
from lib import ui
from faker import Faker

# Programa Principal
quantidade = int(input('Digite a quantidade de nomes: '))
nomes = list()
fake = Faker()
for _ in range(quantidade):
    nome = fake.name()
    nomes.append(nome)
ui.resultado(nomes, fim='; ')