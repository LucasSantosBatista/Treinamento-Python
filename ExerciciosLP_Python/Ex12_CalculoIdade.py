# Receba o ano de nascimento e o ano atual.
# Calcule e mostre a sua idade e quantos anos terá daqui a 17 anos.
from datetime import date

print('Descobra qual será sua idade após 17 anos')

anoNasc: int = int(input('Digite seu ano de nascimento: '))

anoFuturo = date.today().year + 17

idadeFutura = (anoFuturo - anoNasc)

print('No ano de ' + str(anoFuturo) + ' você terá ' + str(idadeFutura) + ' anos.')

