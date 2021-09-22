###########---FUNCTIONS---###########

def menu():
    print("--"*10)
    print("-----RECICLAGEM-----")
    print("--"*10)
    print("\n")
    print("--------MENU--------")
    print("1.LOCAIS PROXIMOS COM BASE EM SUAS COORDENADAS")
    print("2.")
    print("3.")

def primeiraOpcao():
    print("COORDENADAS DEVEM SER INSERIDAS APENAS EM GRAUS DECIMAIS!! (Ex:. x = 37.7 y = -122.2 \n")

    X = float(input("Digite a coordenada X: "))
    Y = float(input("Digite a coordenada Y: "))

    location = pegaLocalizacao()

def segundaOpcao():
    return

def terceiraOpcao():
    return

def pegaLocalizacao():
    return
#####################################

###########---MAIN PROGRAM---###########
menu()

opcaoEscolhida = int(input("Digite uma das opções: "))

if(opcaoEscolhida == 1):
    primeiraOpcao()
elif(opcaoEscolhida == 2):
    segundaOpcao()
elif(opcaoEscolhida == 3):
    terceiraOpcao()

#######################################