from __future__ import annotations
from abc import ABC


class Mediador(ABC):
    """
    A interface Mediador declara um método usado pelos componentes para notificar o
    mediador sobre vários eventos. O Mediador pode reagir a esses eventos e
    passar a execução para outros componentes.
    """

    def notificar(self, remetente: object, evento: str) -> None:
        pass


class MediadorConcreto(Mediador):
    def __init__(self, componente1: Componente1, componente2: Componente2) -> None:
        self._componente1 = componente1
        self._componente1.mediador = self
        self._componente2 = componente2
        self._componente2.mediador = self

    def notificar(self, remetente: object, evento: str) -> None:
        if evento == "A":
            print("O mediador reage a A e aciona as seguintes operações:")
            self._componente2.fazer_c()
        elif evento == "D":
            print("O mediador reage a D e aciona as seguintes operações:")
            self._componente1.fazer_b()
            self._componente2.fazer_c()


class ComponenteBase:
    """
    O Componente Base fornece a funcionalidade básica de armazenar uma instância do mediador
    dentro dos objetos de componente.
    """

    def __init__(self, mediador: Mediador = None) -> None:
        self._mediador = mediador

    @property
    def mediador(self) -> Mediador:
        return self._mediador

    @mediador.setter
    def mediador(self, mediador: Mediador) -> None:
        self._mediador = mediador


"""
Componentes Concretos implementam várias funcionalidades. Eles não dependem de outros
componentes. Também não dependem de nenhuma classe concreta de mediador.
"""


class Componente1(ComponenteBase):
    def fazer_a(self) -> None:
        print("Componente 1 faz A.")
        self.mediador.notificar(self, "A")

    def fazer_b(self) -> None:
        print("Componente 1 faz B.")
        self.mediador.notificar(self, "B")


class Componente2(ComponenteBase):
    def fazer_c(self) -> None:
        print("Componente 2 faz C.")
        self.mediador.notificar(self, "C")

    def fazer_d(self) -> None:
        print("Componente 2 faz D.")
        self.mediador.notificar(self, "D")


if __name__ == "__main__":
    # O código do cliente.
    c1 = Componente1()
    c2 = Componente2()
    mediador = MediadorConcreto(c1, c2)

    print("O cliente aciona a operação A.")
    c1.fazer_a()

    print("\n", end="")

    print("O cliente aciona a operação D.")
    c2.fazer_d()
