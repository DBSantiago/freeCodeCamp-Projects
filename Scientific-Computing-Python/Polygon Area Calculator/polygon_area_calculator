class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        line = 'Rectangle(width={}, height={})'.format(self.width,self.height)
        return line

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        area = self.width * self.height
        return area

    def get_perimeter(self):
        perimeter = 2 * (self.width + self.height)
        return perimeter

    def get_diagonal(self):
        diagonal = (self.width ** 2 + self.height ** 2) ** 0.5
        return diagonal

    def get_picture(self):
        picture = ''
        if self.width > 50 or self.height > 50:
            message = 'Too big for picture.'
            return message
        else:
            for h in range(self.height):
                picture += '*' * self.width + '\n'
        
        return picture

    def get_amount_inside(self,shape):
        fits = 0
        if shape.width > self.width or shape.height > self.height:
            return fits
        else:
            times_width = self.width // shape.width
            times_height = self.height // shape.height
            if times_height == 0 or times_width == 0:
                return fits
            else:
                fits = times_height * times_width
                return fits
        


class Square(Rectangle):
    def __init__(self, length):
        self.width = length
        self.height = length

    def __str__(self):
        line = 'Square(side={})'.format(self.width)
        return line
    
    def set_side(self, length):
        self.width = length
        self.height = length

    def set_width(self,length):
        self.width = length
        self.height = length

    def set_height(self,length):
        self.width = length
        self.height = length
