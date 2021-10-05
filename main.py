###########---BIBLIOTÉCAS---##########
from math import dist
from geopy import geocoders
from geopy.geocoders import Nominatim

#####################################
#######---VARIAVEIS GLOBAIS---######
TIPOS_LIXOS_POSSIVEIS = ["Plastico", "Papel", "Papelao", "Vidro", "Residuos Organico", "Metal", "Madeira", "Residuos Perigosos", "Residuos Hospitalar", "Residuos Radioativos"]
###################################
###########---FUNÇÕES---###########
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
    print("COORDENADAS DEVEM SER INSERIDAS APENAS EM GRAUS DECIMAIS!! (Ex:. x = 37.7 y = -122.2) \n")

    x = float(input("Digite a longitude (X): "))
    y = float(input("Digite a latitude (Y): "))

    tipoReciclavel = str(input("Digite o tipo de reciclável desejado: "))

    if(verificaTipoReciclavel(tipoReciclavel)):
        pontoPossivel = encontraPontoPossivelColeta(x, y, tipoReciclavel)
        print("O local mais adequado para se levar seu lixo é: ",pontoPossivel)
    else:
        print("Tipo de reciclável não encontrado... verifique os dados digitados...")
    

def segundaOpcao():
    return

def terceiraOpcao():
    
    return

def encontraPontoPossivelColeta(x, y, tipoReciclavel):

    pontosColetaDisponiveisX = [-47.20101,-47.10179,-47.09596,-47.07570,-47.05579,-46.97889]
    pontosColetaDisponiveisY = [-22.78100,-22.81139,-22.84050,-22.84651,-22.90345,-22.93001]

    distanciaUsuarioColeta = []

    for i in range(len(pontosColetaDisponiveisX)):
        
        distanciaXY = (((x - pontosColetaDisponiveisX[i])**2 + (y - pontosColetaDisponiveisY[i])**2)**2)

        distanciaUsuarioColeta.append(distanciaXY)

    menorDistancia = min(distanciaUsuarioColeta)

    posicaoXY = distanciaUsuarioColeta.index(menorDistancia)

    localizacaoMaisProxima = encontraLocalizacao(pontosColetaDisponiveisX[posicaoXY], pontosColetaDisponiveisY[posicaoXY])

    return localizacaoMaisProxima

def encontraLocalizacao(x, y):
    
    localizador = Nominatim(user_agent="LearningGeocode")

    return localizador.reverse(str(y)+","+str(x))

def verificaTipoReciclavel(tipoReciclavel):
    tipoLixoExistente = False

    for i in range(len(TIPOS_LIXOS_POSSIVEIS)):
        if(TIPOS_LIXOS_POSSIVEIS[i].upper() == tipoReciclavel.upper()):
            tipoLixoExistente = True
            break
    
    return tipoLixoExistente
########################################
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