#!/usr/bin/python3


from base import Base

class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__y = y
        self.__x = x
        super().__init__(id)

        @property
        def width(self):
            return self.__width
        @width.setter
        def width(self, value):
            if type(value) is not int:
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError("width must be >=0")
            self.__width = value
        @property
        def height(self):
            return self.__height
        @height.setter
        def height(self, value):
            if type(value) is not int:
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError("width must be >=0")
            self.__height = height
        @property
        def x(self):
            return self.__x
        @x.setter
        def x(self, value):
            if type(value) is not int:
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError("width must be >=0")
            self.__x = x
        @property
        def y(self):
            return self.__y
        @x.setter
        def y(self, value):
            if type(value) is not int:
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError("width must be >=0")
            self.__y = y
