import random
import time
itens = ['PEDRA','PAPEL','TESOURA']
print('''SUAS OPÇÕES:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
computador = random.randint(0,2)
player = int(input('Qual é a sua jogada?'))
print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PO!!!')
print('\033[34m=\033[m' *25)
print('O computador escolheu {} \nO Palyer escolheu {}'.format(itens[computador],itens[player]))
print('\033[34m=\033[m' *25)
if computador == 0:
    if player == 0:
        print('\033[32mEMPATE')
    elif player == 1:
        print('\033[35mVOCÊ VENCEU')
    elif player == 2:
        print('\033[31mVOCÊ PERDEU')
    else:
        print('Jogada invalida')
elif computador == 1:
    if player == 0:
        print('\033[31mVOCÊ PERDEU')
    elif player == 1:
        print('\033[32mEMPATE')
    elif player == 2:
        print('\033[35mVOCÊ VENCEU')
    else:
        print('Jogada invalida')
elif computador == 2:
    if player == 0:
        print('\033[35mVOCÊ VENCEU')
    elif player == 1:
        print('\033[31mVOCÊ PERDEU ')
    elif player == 2:
        print('\033[32mEMPATE')
    else:
        print('Jogada invalida')