class Node:

    def __init__(self, name: str):
        self.__name = name
        self.__parents = []
        self.__cpt = {}

    def get_name(self) -> str:
        return self.__name

    def get_parents(self) -> list:
        return self.__parents

    def get_cpt(self) -> dict:
        return self.__cpt