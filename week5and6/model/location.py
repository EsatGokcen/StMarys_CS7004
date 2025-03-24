class Location:
    """
    Represents a point in 2D space.

    Attributes:
        __x (int): The x-coordinate of the location.
        __y (int): The y-coordinate of the location.
    """

    def __init__(self, x: int, y: int) -> None:
        self.__x = x
        self.__y = y

    def get_x(self) -> int:
        return self.__x

    def get_y(self) -> int:
        return self.__y

    def set_x(self, new_x: int) -> None:
        self.__x = new_x

    def set_y(self, new_y: int) -> None:
        self.__y = new_y

    def equals(self, other_location: 'Location') -> bool:
        """
        Checks if two locations are equal.

        Args:
            other_location (Location): The other location to compare.

        Returns:
            bool: True if the locations are equal, False otherwise.
        """
        return self.__x == other_location.get_x() and self.__y == other_location.get_y()

    def __str__(self) -> str:
        return f"({self.__x}, {self.__y})"