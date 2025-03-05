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