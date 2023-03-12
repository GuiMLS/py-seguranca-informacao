import socket
import sys

def main():
    try:
        conexao = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print("A conexão falhou")
        print(f"Erro: {e}")
        sys.exit()

    print("Socket criado com sucesso")

    HostAlvo = input("Digite o host ou IP a ser conectado: ")
    PortaAlvo = input("Digite a porta a ser conectada: ")

    try:
        conexao.connect((HostAlvo, int(PortaAlvo)))
        print(f"Cliente TCP conectado com sucesso no Host {HostAlvo} e na porta {PortaAlvo}")
        conexao.shutdown(2)
    except socket.error as e:
        print(f"A conexão falhou com o seguinte erro: {e}")
        sys.exit()

if __name__ == "__main__":
    main()
