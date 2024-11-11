#Maria Aparecida Gomes
#Gabriel Zacarias 

class Livro:
    def __init__(self, titulo, qtdPag, Pglidas):
        self.titulo = titulo
        self.qtdPag = qtdPag
        self.Pglidas = Pglidas

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo


    @property
    def qtdPag(self):
        return self.__qtdPag

    @qtdPag.setter
    def qtdPag(self, qtdPag):
        self.__qtdPag = qtdPag


    @property
    def Pglidas(self):
        return self.__Pglidas

    @Pglidas.setter
    def Pglidas(self, Pglidas):
        self.__Pglidas = Pglidas


    def verificarProgresso(self):
        if self.__qtdPag > 0:
            progresso = (self.__Pglidas / self.__qtdPag) * 100
            print(f"Você já leu {progresso:.2f} por cento do livro.")
        else:
            print("Erro: O número de páginas do livro não pode ser zero ou negativo.")

def main():

    titulo = input("Digite o título do livro: ")
    qtdPag = int(input("Digite o número total de páginas do livro: "))
    Pglidas = int(input("Digite o número de páginas já lidas: "))


    livro = Livro(titulo, qtdPag, Pglidas)


    novo_qtdPag = int(input("Digite o novo número de páginas do livro: "))
    livro.qtdPag = novo_qtdPag


    print(f"O livro '{livro.titulo}' possui {livro.qtdPag} páginas.")


    novas_Pglidas = int(input("Digite o número de páginas lidas até o momento: "))
    livro.Pglidas = novas_Pglidas


    livro.verificarProgresso()

if __name__ == "__main__":
    main()
