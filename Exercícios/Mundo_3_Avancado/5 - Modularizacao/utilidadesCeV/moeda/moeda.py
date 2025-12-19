def dobro(num, format=False):
    dobro = num * 2
    if format == False:
        return dobro
    else:
        return moeda(dobro)


def metade(num, format=False):
    metade = num / 2
    if format == False:
        return metade
    else:
        return moeda(metade)


def aumento(valor, porcentagem, format=False):
    aumento = (porcentagem / 100 * valor) + valor
    if format == False:
        return aumento
    else:
        return moeda(aumento)


def diminuir(valor, porcentagem, format=False):
    desconto = valor - (porcentagem / 100 * valor)
    if format == False:
        return desconto
    else:
        return moeda(desconto)


def moeda(money):
    moeda = f'R$ {money:.2f}'
    return moeda.replace('.', ',')


