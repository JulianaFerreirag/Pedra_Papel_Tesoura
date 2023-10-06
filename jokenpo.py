
print("   JOKENPÔ   ")
print("Pedra - Papel - Tesoura")
print()
jogador1 = input("Jogador 1 - Digite seu nome: ")
jogador2 = input("Jogador 2 - Digite seu nome: ")
print()
while True:
    escolhaj1 = input(f"{jogador1}  > Pedra - Papel - Tesoura ? ")
    escolhaj2 = input(f"{jogador2}  > Pedra - Papel - Tesoura ? ")
    while escolhaj1 == escolhaj2:
        print(f"< {escolhaj1} X {escolhaj2} > EMPATOU, TENTE NOVAMENTE")
        print()
        escolhaj1 = input(f"{jogador1}  Pedra - Papel - Tesoura ? ")
        escolhaj2 = input(f"{jogador2}  Pedra - Papel - Tesoura ? ")
    if escolhaj1 == "PEDRA" and escolhaj2 == "TESOURA":
        print(f"< {escolhaj1} X {escolhaj2} >  < {escolhaj1} quebra a {escolhaj2} > TEMOS UM VENCEDOR: {jogador1} !!!")
    elif escolhaj1 == "PEDRA" and escolhaj2 == "PAPEL":
        print(f"< {escolhaj1} X {escolhaj2} >  < {escolhaj2} embrulha a {escolhaj1} > TEMOS UM VENCEDOR: {jogador2} !!!")
    elif escolhaj1 == "TESOURA" and escolhaj2 == "PEDRA":
        print(f"< {escolhaj1} X {escolhaj2} >  < {escolhaj2} quebra a {escolhaj1} > TEMOS UM VENCEDOR: {jogador2} !!!")
    elif escolhaj1 == "TESOURA" and escolhaj2 == "PAPEL":
        print(f"< {escolhaj1} X {escolhaj2} >  < {escolhaj1} corta o {escolhaj2} > TEMOS UM VENCEDOR: {jogador1} !!!")
    elif escolhaj1 == "PAPEL" and escolhaj2 == "PEDRA":
        print(f"< {escolhaj1} X {escolhaj2} >  < {escolhaj1} embrulha a {escolhaj2} > TEMOS UM VENCEDOR: {jogador1} !!!")
    elif escolhaj1 == "PAPEL" and escolhaj2 == "TESOURA":
        print(f"< {escolhaj1} X {escolhaj2} >  < {escolhaj2} corta o {escolhaj1} > TEMOS UM VENCEDOR: {jogador2} !!!")
    print()
    Nova_Partida = input("Você deseja continuar jogando ? [S] para 'SIM' ou [N] para 'NÃO'' :")
    print()
    if Nova_Partida in "Nn":
        break
print("Partida encerrada com sucesso! Até breve.")
