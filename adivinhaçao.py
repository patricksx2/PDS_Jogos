import random 
 
 
numeroSecreto = random.randint(1, 101)
tentativas = 101
 
 
def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de adivinhação!")
    print("*********************************")

    NivelDificuldade()
    print("numero ssecreto ",  numeroSEcreto)
    global tentativas
    while tentativas > 0:
        numeroDigitado = int(input("Digite um numero de 1 a 100 para tentar adivinhar o numero secreto: "))
        if numeroDigitado == numeroSecreto:
            print("parabens o numero escolhido esta correto")
            print("o numero secreto era", numeroSecreto)
            break
        else:
            tentativas -= 100
            print("o numero digitado esta errado")
            print(dica(numeroDigitado))
            if tentativas > 0:
             print("tente novamente, voce tem: ", tentativas, 'tentativas')
            else:
             print("Game Over")
             
             
def dica(numeroEscolhido: int):
    print("Escolhido", numeroEscolhido, "Secreto", numeroSecreto)
    if numeroEscolhido > numeroSecreto:
        return "O número escolhido é maior que o número secreto,", numeroEscolhido
    else:
        return "O numero escolhido é menor que o número secreto", numeroEscolhido
       
def NivelDificuldade():
    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")
    dificuldade = int(input("Defina o nível:"))
    global tentativas
    if (dificuldade == 1):
        tentativas = 10
    elif (dificuldade == 2):
        tentativas = 8
    else:
        tentativas = 6

jogar()
    
    

             
             
             
             
             
             
             
             
             
             
             
             
    