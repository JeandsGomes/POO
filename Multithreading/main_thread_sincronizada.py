import threading
from thread_sincronizada import myThread

def main():

    #sinc sera a variavel de sincronização
    sinc = threading.Lock()

    # Create new threads
    thread1 = myThread("Thread-1", 15,1,sinc)
    thread2 = myThread("Thread-2", 15,1,sinc)

    # Start new Threads

    #Thread é executada
    thread1.start()
    thread2.start()

    #comando que faz a espera do termino da thread
    thread2.join()
    thread1.join()

    print("Finalizado a thread principal!")

if __name__=="__main__":
    main()