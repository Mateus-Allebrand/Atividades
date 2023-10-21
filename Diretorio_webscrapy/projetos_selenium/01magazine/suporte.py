import time

def espera(n=15):
    condicao_atendida = False
    tempo_maximo_espera = n
    tempo_inicial = time.time() #Aqui gravei o tempo exato, como se tivesse tirado um *print da hora


    while not condicao_atendida:
        time.sleep(1)

        if time.time() - tempo_inicial >= 7:#Aqui estou comparando o tempo atual real com o meu *print da hora
            condicao_atendida = True
            print("Sucesso!")

        if time.time() - tempo_inicial >= tempo_maximo_espera:
            print("Tempo maximo de espera atingido.\nCondição Não Atendida")
            break



        
        
    

        