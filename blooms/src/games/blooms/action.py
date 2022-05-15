class BloomsAction:
    def __init__(self, x: int, y: int, color: int, num: int, x1: int, y1: int):
        self.__x = x
        self.__y = y
        self.__x1 = x1
        self.__y1 = y1
        self.__color = color
        self.__num = num

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_c(self):
        return self.__color

    def get_num(self):
        return self.__num

    def get_x1(self):
        return self.__x1

    def get_y1(self):
        return self.__y1