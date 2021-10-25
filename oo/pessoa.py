from typing import Mapping


class Pessoa:
    def __init__(self, nome=None, idade=35):
        self.nome = nome
        self.idade = idade

    def cumprimentar(self):
        return f'Olá, {id(self)}'


if __name__ == '__main__':
    p = Pessoa('Fernanda')
    print(p.cumprimentar())
    p.nome = 'Marcelo'
    print(p.nome)
    print(p.idade)
