from typing import Mapping


class Pessoa:
    def __init__(self, *filhos, nome=None, idade=35):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá, {id(self)}'


if __name__ == '__main__':
    marcelo = Pessoa(nome='Marcelo')
    fernanda = Pessoa(marcelo, nome='Fernanda')
    print(Pessoa.cumprimentar(fernanda))
#    p.nome = 'Marcelo'
    print(id(fernanda))
    print(fernanda.cumprimentar())
    print(fernanda.nome)
    print(fernanda.idade)
    for filho in fernanda.filhos:
        print(filho.nome)
