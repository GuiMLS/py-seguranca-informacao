import socket
import sys

conexao = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Socket criado com sucesso!")

host="localhost"
porta = 5432

conexao.bind((host, porta))
mensagem = "Servidor: Olá, Cliente!"

while 1:
    dados, endereco = conexao.recvfrom(4096)
    if dados:
        print("Servidor enviando mensagem")
        #conexao.sendto(dados + (mensagem.encode()), endereco)
        conexao.sendto(mensagem.encode(), endereco)