import os  # Importa módulo os, que usa recursos nativos do SO


ip_ou_host = input("Digite o IP ou Host a ser verificado: ")
print(f"Pingando o IP/Host {ip_ou_host}:")
os.system(f'ping -n 6 {ip_ou_host}')
