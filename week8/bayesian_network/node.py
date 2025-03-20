from typing import Self

class Node:

    def __init__(self, name: str):
        self.__name = name
        self.__parents = []
        self.__cpt = {}

    def get_name(self) -> str:
        return self.__name

    def get_parents(self) -> list[Self]:
        return self.__parents

    def get_cpt(self) -> dict[bool | float]:
        return self.__cpt

    def add_parent(self, parent_node: Self):
        self.__parents.append(parent_node)

    def remove_parent(self, parent_node: Self):
        self.__parents.remove(parent_node)