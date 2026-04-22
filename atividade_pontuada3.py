import os 
os.system("cls")




avioes = [0, 0, 0, 0]     
assentos = [0, 0, 0, 0]  
reservas = []             
contador_reservas = 0     

print("Sweet Flight - Sistema de Reservas")

while True:
    print()
    print("1 - Cadastrar aviões")
    print("2 - Cadastrar assentos")
    print("3 - Reservar")
    print("4 - consulta de avião")
    print("5 - consulta de passageiro")
    print("6 - Sair")
    
    opcao = input("Digite uma opção: ")
    
    
    if opcao == "1":
        print("Digite o numero dos aviões: ")
        for i in range(4):
            avioes[i] = int(input("Avião " + str(i+1) + ": "))
        print("AVIÕES OK!")
    
    
    elif opcao == "2":
        print("Digite numero de assentos de cada avião: ")
        for i in range(4):
            assentos[i] = int(input("Avião " + str(avioes[i]) + ": "))
        print("ASSENTOS OK!")
    
    
    elif opcao == "3":
        if contador_reservas >= 20:
            print("LIMITE DE 20 RESERVAS!")
            continue
        
        num_aviao = int(input("Número do avião: "))
        
        
        existe = False
        posicao = -1
        for i in range(4):
            if avioes[i] == num_aviao:
                existe = True
                posicao = i
                break
        
        if not existe:
            print("Este avião não existe!")
            continue
        
        
        if assentos[posicao] == 0:
            print("Não há assentos disponíveis para este avião!")
            continue
        
        
        nome = input("Nome do passageiro: ")
        reservas.append([num_aviao, nome])
        assentos[posicao] = assentos[posicao] - 1
        contador_reservas = contador_reservas + 1
        print("Reserva realizada com sucesso!")
    
    
    elif opcao == "4":
        num_aviao = int(input("Número do avião para consulta: "))
        
        
        existe = False
        for i in range(4):
            if avioes[i] == num_aviao:
                existe = True
                break
        
        if not existe:
            print("Este avião não existe!")
            continue
        
        
        tem_reserva = False
        print("Passageiros:")
        for r in reservas:
            if r[0] == num_aviao:
                print("- " + r[1])
                tem_reserva = True
        
        if not tem_reserva:
            print("Não há reservas realizadas para este avião!")
    
    
    elif opcao == "5":
        nome = input("Nome do passageiro para consulta: ")
        
        tem_reserva = False
        print("Aviões reservados deste passageiro:")
        for r in reservas:
            if r[1] == nome:
                print("- Avião " + str(r[0]))
                tem_reserva = True
        
        if not tem_reserva:
            print("Não há reservas realizadas para este passageiro!")
    
    
    elif opcao == "6":
        print("Encerrando sistema...!")
        break
    
    else:
        print("Opção errada!")