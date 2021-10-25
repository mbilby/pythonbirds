from typing import Mapping


class Pessoa:

    olhos = 2

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
    fernanda.sobrenome = 'Rodrigues'
    fernanda.olhos = 1
    del fernanda.olhos
    print(fernanda.__dict__)
    print(marcelo.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(fernanda.olhos)
    print(marcelo.olhos)
    print(id(Pessoa.olhos), id(fernanda.olhos), id(marcelo.olhos))
