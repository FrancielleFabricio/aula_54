import time

numero_inteiro = input('digite um numero inteiro: ')
if numero_inteiro.isnumeric():
    if int(numero_inteiro) % 2 == 0:
        print(f'O número {numero_inteiro} é par')
    else:
        print(f'O número {numero_inteiro} é impar')
else:
    print(f'Você digitou " {numero_inteiro.upper()} " e isso não é valido')
    time.sleep(1)
    print('Por favor digite um numero inteiro'.upper())