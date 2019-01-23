class Livraria:

    bd_livraria = {}
    lista = []
    lista_temporaria = []

    def __init__(self, idd, nome, escritor):

        self.isbn = idd
        self.titulo = nome
        self.autor = escritor

    def registrolivro(self, valor):
        self.isbn = valor
        a.lista = a.lista_temporaria.copy()
        a.bd_livraria[a.isbn] = a.lista
        a.lista.append(str(a.autor))
        a.lista.append(str(a.titulo))


        return self.isbn


a = Livraria(idd='', nome='', escritor='')

while True:
    print('')
    print('\033[7;30mCADASTRAR NOVO LIVRO\033[m\n')
    print('N - Novo Cadastro\nR - Relatório\nA - Apagar\nS - Sair')
    print('')

    op = str(input('Escolha uma opção: ')).upper()

    if op == 'N':
        print('\nInforme o ISBN do livro que deseja cadastrar: ')
        a.isbn = int(input('ISBN: '))

        if a.isbn in a.bd_livraria:
            print('>> ISBN - \033[33mEXISTENTE\033[m <<')
            print('>> CADASTRO \033[7mNÃO\033[m REALIZADO <<')
            continue

        a.titulo = str(input('Título: ')).upper()
        a.autor = str(input('autor: ')).upper()
        a.registrolivro(a.isbn)  # invoca a função isbn - Sem isso, NÂO funciona

    elif op == 'r'.upper():
        if a.bd_livraria == {}:
            print('\n-- \033[31mCadastro Vazio\033[m --')
        else:
            print('')
            y = a.bd_livraria.items()
            for k, v in y:
                print('ISBN: ', k, end=" - ")
                print('\033[30mLIVRO:\033[m ', v[1], end=" - ")
                print('\033[30mAUTOR:\033[m ', v[0])

    elif op == 'a'.upper():
        print('\nInforme o ISBN do livro que deseja APAGAR: ')
        a.isbn = int(input('ISBN: '))

        if a.isbn in a.bd_livraria:
            del a.bd_livraria[a.isbn]
        else:
            print('>>> ISBN não encontrado! <<<')

    elif op == 's'.upper():
        print('Sair')
        exit()


