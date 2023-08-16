import math

class Rectangle:

        def __init__(self, width, height):
            self.width = width
            self.height = height

        def __str__(self):
            return "Rectangle(width={}, height={})".format(self.width, self.height)

        def set_width(self, width):
            self.width = width

        def set_height(self, height):
            self.height = height

        def get_area(self):
            return self.width * self.height

        def get_perimeter(self):
            return 2 * self.width + 2 * self.height

        def get_diagonal(self):
            return (self.width ** 2 + self.height ** 2) ** .5

        def get_picture(self):
            if self.height > 50 or self.width > 50:
                return("Too big for picture.")
            else:
                count = 0
                return_str = ""
                for i in range (0, self.height):
                    return_str += "*" * self.width + "\n"
                    count += 1
                return return_str

        def get_amount_inside(self, shape):

            #print("shape ->" +str(shape.width), str(shape.height))
            #print("self ->" + str(self.width), str(self.height))
            height_ratio = shape.height / self.height
            #print("height ratio "+str(height_ratio) )
            width_ratio = shape.width / self.width
            #print("width ratio " + str(width_ratio))
            times_height = math.floor(1 / height_ratio)
            times_width = math.floor(1 / width_ratio)
            return times_width * times_height

class Square(Rectangle):

        def __init__(self , length, width = 0, height = 0 ):
            super().__init__(width, height )
            self.height = length
            self.width = length
            self.length = length

        def __str__(self):
            return "Square(side={})".format(self.length)

        def set_side(self, length):
            self.length = length
            self.width = length
            self.height = length

        def set_width(self, width):
            self.length = width

        def return_length(self):
            return self.height
