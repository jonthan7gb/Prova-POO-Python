from TransportePublico import Transporte
from TransportePublico import Onibus
from TransportePublico import Trem
from TransportePublico import Metro
from TransportePublico import mostrarMenu
import time as t

ListaTransportes = []
escolha = 0
ids = 1
removido = False

#Cadastrando alguns objetos

onibus = Onibus("Onibus", ids, 100, "Linha Verde", "Executivo")
ListaTransportes.append(onibus)
ids = ids + 1

trem = Trem("Trem", ids, 200, "Linha Amarela", 20)
ListaTransportes.append(trem)
ids = ids + 1

metro = Metro("Metrô", ids, 500, "Linha Azul", True)
ListaTransportes.append(metro)

while escolha != 4:
    mostrarMenu()
    escolha = int(input("? - Sua escolha: "))
    removido = False

    match escolha:
        case 1:
            t.sleep(0.5)
            print("\n== Tipo de Transporte ==")
            print("1 - Onibus")
            print("2 - Trem")
            print("3 - Metrô")
            escolhaVeiculo = int(input("? - Sua escolha: "))

            match escolhaVeiculo:
                case 1:
                    t.sleep(0.5)
                    print("\n==== Cadastrar Onibus ====")
                    capacidadePass = int(input("? - Capacidade de passageiros do onibus: "))
                    linhaOpe = input("? - Nome ou número da linha de operação: ")
                    tipoOnibus = input("? - Tipo do onibus (Convencional ou Executivo): ")
                    ids = ids + 1
                    transpTipo = "Onibus"

                    if tipoOnibus == "Convencional" or tipoOnibus == "Executivo" or tipoOnibus == "convencional" or tipoOnibus == "executivo":
                        onibusObj = Onibus(transpTipo, ids, capacidadePass, linhaOpe, tipoOnibus)
                        ListaTransportes.append(onibusObj)

                        print("\n-- Onibus cadastrado com sucesso --\n")

                    else:
                        print("\n== Tipo de onibus inválido ==\n")

                case 2:
                    t.sleep(0.5)
                    print("\n==== Cadastrar Trem ====")
                    capacidadePass = int(input("? - Capacidade de passageiros do trem: "))
                    linhaOpe = input("? - Nome ou número da linha de operação: ")
                    numVagoes = input("? - Número total de vagões: ")
                    ids = ids + 1
                    transpTipo = "Trem"

                    tremObj = Trem(transpTipo, ids, capacidadePass, linhaOpe, numVagoes)
                    ListaTransportes.append(tremObj)
                    
                    print("\n-- Trem cadastrado com sucesso --\n")

                case 3:
                    t.sleep(0.5)
                    print("\n==== Cadastrar Metrô ====")
                    capacidadePass = int(input("? - Capacidade de passageiros do metrô: "))
                    linhaOpe = input("? - Nome ou número da linha de operação: ")
                    subterraneoSN = input("? - É subterraneo? (Sim | Não): ")
                    ids = ids + 1
                    transpTipo = "Metrô"

                    if subterraneoSN == "Sim":
                        subterraneoSN = True
                    else:
                        subterraneoSN = False

                    metroObj = Metro(transpTipo, ids, capacidadePass, linhaOpe, subterraneoSN)
                    ListaTransportes.append(metroObj)
                    
                    print("\n-- Metrô cadastrado com sucesso --\n")

                case _:
                    print("\n=== Escolha inválida ===\n")
                    
                      
        case 2:
            t.sleep(0.5)
            print("\n==== Listar Transportes ====")
            print("1 - Todos")
            print("2 - Onibus")
            print("3 - Trens")
            print("4 - Metrôs")
            escolhaPesquisa = int(input("? - Sua escolha: "))
            print("")
            t.sleep(0.5)
            match escolhaPesquisa:
                case 1:
                    print(35 * "=")
                    for transporte in ListaTransportes:
                        transporte.exibir_status()    
                        t.sleep(1)
                    print("")

                case 2:  
                    print(35 * "=")
                    for transporte in ListaTransportes:
                        if transporte.transp == "Onibus":
                            transporte.exibir_status()     
                            t.sleep(1)        
                    print("")

                case 3:  
                    print(35 * "=")
                    for transporte in ListaTransportes:
                        if transporte.transp == "Trem":
                            transporte.exibir_status()  
                            t.sleep(1)           
                    print("")

                case 4:  
                    print(35 * "=")
                    for transporte in ListaTransportes:
                        if transporte.transp == "Metrô":
                            transporte.exibir_status()  
                            t.sleep(1)           
                    print("")
                
                case _:
                    print("=== Escolha inválida ===\n")

        case 3:
            t.sleep(0.5)
            print("\n==== Remover Transporte ====")
            transporteRemover = int(input("? - Insira o id do transporte que deseja remover: "))


            for transporte in ListaTransportes:
                if transporteRemover == transporte.id:
                    print("")
                    t.sleep(1)
                    print(35 * "=")
                    
                    transporte.exibir_status()
                    t.sleep(1)
                    ListaTransportes.remove(transporte)
                    removido = True
                    print("\n==== Transporte removido com sucesso ====\n")
                    t.sleep(1)

            if removido == False:
                t.sleep(1)
                print("\n== Nenhum Transporte Cadastrado nesse ID ==\n") 
                t.sleep(1)
            

        case 4:
            t.sleep(1)
            print("==== Saindo do Programa ====")
            t.sleep(1)
        case _:
            print("\n=== Escolha inválida ===\n")