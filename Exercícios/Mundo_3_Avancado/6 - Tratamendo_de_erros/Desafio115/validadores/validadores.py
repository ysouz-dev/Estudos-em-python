from Desafio115.cores import cores

cor = cores.cores()


def validador_de_numero(tipo, message, message_error):
    while True:
        try:
            numero = tipo(input(message))
        except:
            print(f'{cor[1]}{message_error}{cor[0]}')
        else:
            return numero


def validador_de_string(message, message_error):
    while True:
        string = str(input(message)).strip()
        if string.replace(' ', '').isalpha() == True:
            return string
        else:
            print(f'{cor[1]}{message_error}{cor[0]}')
