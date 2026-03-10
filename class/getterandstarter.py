from datetime import datetime

class Rectangle:
    def __init__(self, length, width):
        if not isinstance(length, (int, float)):
            raise TypeError("Length must be a number.")
        if not isinstance(width, (int, float)):
            raise TypeError("Width must be a number.")

        self._length = length
        self._width = width

    @property
    def length(self):
        return self._length
    
    @length.setter
    def length(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Length must be a number.")
        self._length = value

    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Width must be a number.")
        self._width = value

    def area(self):
        sol = self.length * self.width
        print(f"The area of the rectangle with length {self.length} and width {self.width} is {sol}")
        return sol

    def define_width(self, width):
        now = datetime.now()
        print(f"The width was {self.width} at {now}")
        self.width = width
        return f"Width updated to {width}"
    
    def draw(self):
        length =self.length
        width = self.width
        for i in range [width]:
            asteric = "*" * length
            print(asteric)

# Example usage
rl = Rectangle(length=30, width=35)
print(rl.__dict__)

rl_width = rl.define_width(width=70)
print(rl_width)

print(rl.__dict__)
rl.area()
