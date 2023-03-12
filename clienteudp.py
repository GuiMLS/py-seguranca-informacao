import socket

conexao = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Cliente Socket Criado com sucesso!")

host = 'localhost'
porta = 5433
mensagem = "Olá servidor!"

try:
    print(f"Cliente: Tentando enviar a mensagem: {mensagem}")
    conexao.sendto(mensagem.encode(), (host, 5432))

    dados, servidor = conexao.recvfrom(4096)
    dados = dados.decode()
    print(f"Cliente: Dados recebidos - {dados}")
finally:
    print("Cliente: Fechando a Conexão")
    conexao.close()
