#Faça um programa de implemente um jogo de Craps. O jogador lança um par de dados,
#obtendo um valor entre 2 e 12. Se, na primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou.
#Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e você perdeu devendo R$ 10.000 para a Nat
#e para o Groger. Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10, você perdeu não devendo nada para nós.

import random
def jogo_craps():
    dado1 = int(random.randint(1,6))
    dado2 = int(random.randint(1,6))
    soma = dado1 + dado2
    print(soma)
    if soma ==7 or soma ==11:
        return 'Você ganhou!'
    elif soma ==2 or soma ==3 or soma ==12:
        return 'Craps: você perdeu e deve R$10.000 para a Nat e Groger'
    else:
        return 'Você perdeu, mas não deve nada'

print(jogo_craps())

