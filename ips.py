import ipaddress

ip = "192.168.0.1"

endereco = ipaddress.ip_address(ip)
# SOMA no formato de IPs (zerando em 255 e incrementando no campo à esquerda):
print(endereco + 257)

#Notação CIDR e também checa se esse IP é válido para a rede (IP 0). Caso haja um ip 192.168.10/24 PARA REDE (network), ele retornará um erro.
ip = "192.168.0.0/24"
rede = ipaddress.ip_network(ip)
print(rede)

#Retirando o erro de network para caso seja interessante detectar isso sem gerar erro, mas ele corrige para o endereço 0 mesmo assim:
ip = "192.168.0.10/24"
rede = ipaddress.ip_network(ip, strict=False)
print(rede)

#IMPRIMIR TODOS OS IPS DA REDE:
ip = "192.168.0.0/24"
rede = ipaddress.ip_network(ip, strict=False)
for ip in rede:
    print(ip)
#Observe que, por ser /24, há apenas 2^8 IPs na rede (2^8 = 256).

