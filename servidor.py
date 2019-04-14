from socket import *
from cryptography.fernet import Fernet

file = open('key.key', 'rb')
key = file.read()
file.close()

host = '' #endereço da máquina servidor
porta = 80

servidor_socket = socket(AF_INET, SOCK_STREAM) #SOCK_STREAM = TCP; AF_INET = IP; Server TCP/IP

servidor_socket.bind((host, porta)) #vincula o servidor a porta; .bind significa que esse é o serivdor
servidor_socket.listen(10) #numero de conexoes por vez
print("Aguardando conexao...")

while True:
    conexao, endereco = servidor_socket.accept() #aceita a conexao
    print ("Servidor conectado por {}".format(endereco)) #imprime o end. do cliente conectado
    print ("Aguardando mensagem...")

    while True:

        data = conexao.recv(1024) #recebe uma mensagem de até 1024 bytes
        f = Fernet(key)
        decrypted = f.decrypt(data)
        original_message = decrypted.decode()
        print("Mensagem recebida")
        print(original_message)

        if not data: #se não receber nada, para o loop
            break
            conexao.send(bytes('Eco=>' + data)) #o servidor manda de volta uma resposta ao cliente

    conexao.close() #fecha a conexao depois de responder ao cliente