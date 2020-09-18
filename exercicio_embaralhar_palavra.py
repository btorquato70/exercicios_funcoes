def embaralha(): #Defini a funçao embaralha
    palavra = input("Digite uma palavra: ")
    import random #Importa a biblioteca random
    embaralhador = random.sample(palavra, len(palavra))
    palavra_embaralhada = ''.join(embaralhador)  # Transforma a lista em string
    return palavra_embaralhada.upper()  # pode usar o .lower() também (Altera o formato das letras)

print(embaralha())