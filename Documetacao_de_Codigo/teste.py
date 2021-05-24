

class Exercicio_Documetacao():

    def __init__(self):
        pass

    def teste_de_documentacao(self):
        """Summary or Description of the Function
        mostar um testo qualquer:
            argumentos;
        """
        print('ola')


def main():
    exercicio=Exercicio_Documetacao()
    help(exercicio.teste_de_documentacao)


if __name__=='__main__':
    main()