import socket, sys

def main():
    try:
        #protocolo IP, TCP, protocolo de comunicação com o servidor
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        
    except socket.error as erro:
        print('falha na conecção')
        print(f"error: {erro}")
        sys.exit()
        
    print('Socket criado com sucesso')
    
    host_alvo = input("digite o ip ou host a ser conectado: ")
    porta_alvo = int(input('digite a porta a ser conectada: '))
    
    try:
        s.connect((host_alvo, porta_alvo))
        print(f'client TCP conectado com sucesso host: {host_alvo} e na porta: {porta_alvo}')
        s.shutdown(2)
    
    except socket.error as erro:
        print(f'não foi possivel se conectar no host: {host_alvo} e porta: {porta_alvo}')
        print(f'error: {erro}')
        sys.exit()
        
if __name__ == '__main__':
    main()