from abc import ABC, abstractmethod
from sys import exit

class Associa(ABC):
    @abstractmethod
    def relacionar(self, nome):
        pass
# class associa serve de base para as associacoes

class Aluno(Associa):
    def relacionar(self, nome):
        return f"{nome} é um aluno na Fatec."

class Professor(Associa):
    def relacionar(self, nome):
        return f"{nome} é um professor na Fatec."

class Coordenador(Associa):
    def relacionar(self, nome):
        return f"{nome} é um coordenador na Fatec."

class Diretor(Associa):
    def relacionar(self, nome):
        return f"{nome} é um diretor na Fatec."

class Administrador(Associa):
    def relacionar(self, nome):
        return f"{nome} é um administrador na Fatec."

class Vestibulando(Associa):
    def relacionar(self, nome):
        return f"{nome} é um vestibulando na Fatec."

class FabricaAssociacao:
    def criar_assos(self, tipo_assos):
        if tipo_assos == "Aluno":
            return Aluno()
        elif tipo_assos == "Professor":
            return Professor()
        elif tipo_assos == "Coordenador":
            return Coordenador()
        elif tipo_assos == "Diretor":
            return Diretor()
        elif tipo_assos == "Administrador":
            return Administrador()
        elif tipo_assos == "Vestibulando":
            return Vestibulando()

repeat = True
while repeat == True:
    print("\n==MENU== \nDigite 'q' para sair")
    nome = input("Entre com o seu nome: ")
    if nome.lower() == "q":
        exit()
    relac = input("Qual a sua relação com a FATEC: ")

    fabrica_associacao = FabricaAssociacao()
    if relac.lower() == "aluno":
        alun = fabrica_associacao.criar_assos("Aluno")
        print(alun.relacionar(nome))
        #caso do aluno
    elif relac.lower() == "professor":
        prof = fabrica_associacao.criar_assos("Professor")
        print(prof.relacionar(nome))
        #caso do professor
    elif relac.lower() == "coordenador":
        coord = fabrica_associacao.criar_assos("Coordenador")
        print(coord.relacionar(nome))
        #caso do coordenador
    elif relac.lower() == "diretor":
        diret = fabrica_associacao.criar_assos("Diretor")
        print(diret.relacionar(nome))
        #caso do diretor
    elif relac.lower() == "administrador":
        adm = fabrica_associacao.criar_assos("Administrador")
        print(adm.relacionar(nome))
        #caso do administrador
    elif relac.lower() == "vestibulando":
        vestb = fabrica_associacao.criar_assos("Vestibulando")
        print(vestb.relacionar(nome))
        #caso do vestibulando
    else:
        print(f"{nome} não tem relação com a Fatec, siga até a secretaria.")
        #caso nao tenha uma das relacoes acima
