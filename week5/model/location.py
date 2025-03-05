class Location:
    """
    Represents a point in 2D space.

    Attributes:
        __x (int): The x-coordinate of the location.
        __y (int): The y-coordinate of the location.
    """

    def __init__(self, x: int, y: int) -> None:
        """
        Initialises a Location object with given x and y coordinates.

        Args:
            x (int): The x-coordinate of the location.
            y (int): The y-coordinate of the location.
        """
        self.__x = x
        self.__y = y

    def get_x(self) -> int:
        """
        Gets the x-coordinate of the location.

        Returns:
            int: The x-coordinate.
        """
        return self.__x

    def get_y(self) -> int:
        """
        Gets the y-coordinate of the location.

        Returns:
            int: The y-coordinate.
        """
        return self.__y

    def set_x(self, new_x: int) -> None:
        """
        Sets the x-coordinate of the location.

        Args:
            new_x (int): The new x-coordinate.
        """
        self.__x = new_x

    def set_y(self, new_y: int) -> None:
        """
        Sets the y-coordinate of the location.

        Args:
            new_y (int): The new y-coordinate.
        """
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