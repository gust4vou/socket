from socket import *
from cryptography.fernet import Fernet

#pegando a chave no arquivo
file = open('key.key', 'rb')
key = file.read()
file.close()

#transformando em bytes
message = input('Digite a mensagem: ')
encoded = message.encode()

#cifrando a mensagem
f = Fernet(key)
encrypted = f.encrypt(encoded)

server_host = 'localhost' #colocar o endereco ip do servidor
server_port = 80 #colocar porta do servidor

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((server_host, server_port)) #.connect significa que esta tentando se conectar com o servidor

for linha in message:
    client_socket.send(encrypted) #envia a mensagem ao servidor (codificada em bytes)
    print ("Mensagem enviada")

    data = client_socket.recv(1024) #espera uma resposta do servidor
    print("O cliente recebeu amensagem")

client_socket.close() #fecha a conexao