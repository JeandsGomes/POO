import threading
import socket

class ClientThread(threading.Thread):

    def __init__(self,clientAddress,clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        print("Nova conexao: ",clientAddress)

    def run(self):
        print("Conectado de: ", clientAddress)
        msg = ''
        while True:
            data = self.csocket.recv(1024)
            msg = data.decode()
            self.csocket.send(msg.encode())
            print("from client", msg)
            if msg=='bye':
                break
        print("CLent at", clientAddress, " disconnected...")


if __name__=='__main__':

    LOCALHOST = ''
    PORT = 7002
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((LOCALHOST, PORT))
    print("Servidor iniciado!")
    print("Aguardando nova conexao..")
    while True:
        server.listen(1)
        clientsock, clientAddress = server.accept()
        newthread = ClientThread(clientAddress, clientsock)
        newthread.start()
        
    