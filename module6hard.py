from math import pi, sqrt

class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__color = color
        self.__sides = sides

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if 0 < r <= 255 and 0 < g <= 255 and 0 < b <= 255:
            return r, g, b
        else:
            return self.__color

    def set_color(self, r, g, b):
        new_color = self.__is_valid_color(r, g, b)
        self.__color = list(new_color)
        return self.__color

    def _is_valid_sides(self, *new_sides):
        for i in new_sides:
            if i > 0:
                if len(new_sides) == self.sides_count:
                    return True
                else:
                    return False

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        for k in new_sides:
            if k != self.__is_valid_sides(k):
                self.__sides = list(new_sides)
                return self.__sides

class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__sides = sides
        self.__radius = self.__sides[0] / (2 * pi)

    def get_squart(self):
        Sc = (self.__radius ** 2) * pi
        return Sc

class Triangle(Figure):
    sides_count = 3
    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.sides = sides
        p = (self.sides[0] + self.sides[1] + self.sides[2]) / 2
        self.__height = 2 * (sqrt(p * (p - self.sides[0]) * (p - self.sides[1]) * (p - self.sides[2]))) / self.sides[0]

    def get_square(self):
        St = (self.__height * self.sides[0]) / 2
        return St

class Cube(Figure):
    sides_count = 12
    def __init__(self, color, *sides):
         super().__init__(color, *sides)
         self.sides = sides

    def get_volume(self):
        Vc = self.__sides[0] ** 3
        return Vc

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())