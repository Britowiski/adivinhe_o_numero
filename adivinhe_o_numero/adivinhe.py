import random

erros = 0
sorteado = random.randint(0, 100)  

while True:
    jogador = int(input("Tente acertar o número: "))

    if sorteado == jogador:
        erros += 1
        print("Parabéns! Você acertou em", erros, "tentativas.")
        break  
    elif sorteado > jogador:
        print("ERRO, você errou! O número é maior.")
    else:
        print("ERRO, você errou! O número é menor.")

    erros += 1  


print("O número sorteado era:", sorteado)
