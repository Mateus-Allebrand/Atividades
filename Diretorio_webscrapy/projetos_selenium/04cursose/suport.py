import time

#função pause tela





def congela_tempo(tmx=10,t=7):
    condicao_atendida = False
    tempo_inicial = time.time()
    tempo_max_espera = tmx


    while not condicao_atendida:
        time.sleep(1)

        if time.time() - tempo_inicial >= t:
            condicao_atendida = True
            print("Sucesso!")
            break

        if time.time() - tempo_inicial >= tempo_max_espera:
            print("tempo maximo estourado!")
            break
    