import time

numero = input('digite um numero inteiro: ')
if numero.isnumeric():
    numero_inteiro = int(numero)
    if numero_inteiro % 2 == 0:
        print(f'O número {numero} é PAR')
    else:
        print(f'O número {numero} é IMPAR')
else:
    print(f'Você digitou " {numero.upper()} " e isso não é valido')
    time.sleep(1)
    print('Por favor digite um numero inteiro'.upper())