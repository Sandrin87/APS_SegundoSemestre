###########---BIBLIOTÉCAS---##########
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
        pontosPossiveis = encontraPontosPossiveisColeta(x, y, tipoReciclavel)
        print(pontosPossiveis)
    else:
        print("Tipo de reciclável não encontrado... verifique os dados digitados...")
    

def segundaOpcao():
    return

def terceiraOpcao():
    
    return

def encontraPontosPossiveisColeta(x, y, tipoReciclavel):
    
    localizacaoUsuarioCompleta = encontraLocalizacaoUsuario(x, y)

    cidadeUsuario = localizacaoUsuarioCompleta['address']['city_district']



    return cidadeUsuario

def encontraLocalizacaoUsuario(x, y):
    
    localizador = Nominatim(user_agent="LearningGeocode")

    return localizador.reverse(str(y)+","+str(x)).raw

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