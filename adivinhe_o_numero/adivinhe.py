import random

erros = 0
sorteado = random.randint(0, 100)  # Corrigindo para usar randint que inclui o valor superior

while True:
    jogador = int(input("Tente acertar o número: "))

    if sorteado == jogador:
        erros += 1
        print("Parabéns! Você acertou em", erros, "tentativas.")
        break  # Encerra o loop quando o jogador acerta
    elif sorteado > jogador:
        print("ERRO, você errou! O número é maior.")
    else:
        print("ERRO, você errou! O número é menor.")

    erros += 1  # Incrementa o número de erros apenas se o jogador errar

# Fora do loop, após o encerramento do jogo
print("O número sorteado era:", sorteado)
