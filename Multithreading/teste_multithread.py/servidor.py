import threading
import socket
import time

class ClientThread(threading.Thread):

    def __init__(self,clientAddress,clientsocket,sinc):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        self.sinc = sinc
        print("Nova conexao: ",clientAddress)

    def run(self):
        print("Conectado de: ", clientAddress)
        self.sinc.acquire()
        self._codigo=self.operacao_da_thread()
        self.sinc.release()
        print("Finalizando ",clientAddress)
        

    def operacao_da_thread(self):

        msg = ''
        data = self.csocket.recv(1024)
        msg = data.decode()
        self.csocket.send(msg.encode())
        print("CLent at", clientAddress, " disconnected...")
        return msg

    @property
    def codigo(self):
        return self._codigo



if __name__=='__main__':

    LOCALHOST = ''
    PORT = 7002
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((LOCALHOST, PORT))
    print("Servidor iniciado!")
    print("Aguardando nova conexao..")

    sinc = threading.Lock()

    while True:
        server.listen(1)
        clientsock, clientAddress = server.accept()
        newthread = ClientThread(clientAddress, clientsock, sinc)
        newthread.start()
        newthread.join()
        print('codigo >> %s' % newthread.codigo)
        
    