import os  # Importa módulo os, que usa recursos nativos do SO
import re  # Regex
import time

lista_corrigida = []


def pingar(ip_a_pingar):
    print(os.system(f'ping -n 2 {ip_a_pingar}'))
    time.sleep(2)


with open('hosts.txt') as file:
    dump = file.read()
chunks = dump.split('\n')
for elemento in chunks:
    pat = re.compile("\S+\.\S+\.")  # Regex pega apenas itens que são IP/Host.
    test = pat.match(elemento)
    if test:
        lista_corrigida.append(elemento)
        pingar(elemento)
    else:
        print(f"{elemento} não me parece um IP/host. Conserte esse endereço!")
