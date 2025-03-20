from typing import Self

class Node:

    def __init__(self, name: str) -> None:
        self.__name = name
        self.__parents = []
        self.__cpt = {}

    @property
    def name(self) -> str:
        return self.__name

    @property
    def parents(self) -> list[Self]:
        return self.__parents

    @property
    def cpt(self) -> dict[tuple[bool] | float]:
        return self.__cpt

    def add_parent(self, parent_node: Self) -> None:
        self.__parents.append(parent_node)

    def remove_parent(self, parent_node: Self) -> None:
        self.__parents.remove(parent_node)