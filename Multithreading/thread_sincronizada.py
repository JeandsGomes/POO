
import threading
import time

class myThread(threading.Thread):
    def __init__(self,nome,contador,delay,sinc):
        threading.Thread.__init__(self)
        self.nome = nome
        self.contador = contador
        self.delay = delay
        self.sinc = sinc

    def run(self):
        print("Iniciando" + self.nome)
        
        #sera congelado o espaço a baixo
        self.sinc.acquire()
        print_time(self.nome, self.contador, self.delay)

        #libera a função para que outra thread 
        self.sinc.release()
        print("Finalizando "+ self.nome)


def print_time(threadName, contador, delay):
    while contador:
        time.sleep(delay)
        print("{} - {}: {}".format(15-contador,threadName, time.ctime(time.time())))
        contador -= 1
    

'''
Tread
* Executar várias threads é similar a executar prograas ao mesmo tempo;
* Entretanto existem alguns beneficios de se utilizar threads;
    * Multiplas threads em um processo compartilham o mesmo espaço de dados;
    * Dessa forma, ela podem compartilhar informações e se comunicar mais facilmente;
    * Threads são usualmente chamados de processos-leves, ou seja, elas possuem um menor custo 
    computacional que um processo.
* Uma thread possui um inicio, uma sequência de execuções e uma conclusão;
* Uma thread pode:
    * Ser interrompida;
    * Ser colocada em espera.
'''

'''

O módulo threading

* tun() - O método é o ponto de partida para execução de uma thread;
* start() - o método start() inicia a thread chmado o método run();
* join() - o método join() espera a thread terminar;
* isAlive() - esse método verifica se a thread ainda está em execução;
* getName() - retorna o nome da thread.
* setName() - atribui um nome á thread.
* threading.activeCount() - retorna a quantidade de threads ativas.
* threading.enumerate() - retorna uma lista com todas as threads executando 
atualmente.

'''
