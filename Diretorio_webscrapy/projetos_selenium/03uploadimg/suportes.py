import time



def espera(n=10):
    # Condição que queremos verificar
    condicao_atendida = False

    # Tempo máximo de espera em segundos
    tempo_maximo_espera = n  # Por exemplo, aguardar até 10 segundos

    # Tempo inicial
    tempo_inicial = time.time()

    while not condicao_atendida:
        # Verifique a condição a cada 1 segundo (você pode ajustar o intervalo)
        time.sleep(1)  # Espera por 1 segundo
        
        
        # Neste exemplo, suponhamos que a condição seja atendida após 7 segundos
        if time.time() - tempo_inicial >= 7:
            condicao_atendida = True
            print("Condição atendida!")

        # Verifique se o tempo máximo de espera foi atingido
        if time.time() - tempo_inicial >= tempo_maximo_espera:
            print("Tempo máximo de espera atingido. Condição não atendida.")
            break