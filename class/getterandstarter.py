class Rectangle:
    def __init__(self, length, width):
        if not isinstance(length,(int,float)):
            raise TypeError("Length must be an integer ")
        
        if not isinstance(width,(int,float)):
            raise TypeError("Width must be an integer")
        
        self._length = length
        self.width = width

    def area(self):
        sol = self.length * self.width
        print(f"The area of rectagle with length of {self.length} and width of {self.width} is {sol}")
        return sol
    @property
    def length(self):
        return self._length
    @length.setter
    def define_length(self, length):
        if not isinstance(length,(int,float)):
            raise TypeError("Length must be an integer ") 
            #print("THE LENGTH MUST BE A VALUE OR A NUMBER")
        self._length = length    


    def define_width(self, width):        
        if not isinstance(width,(int,float)):
            raise TypeError("Width must be an integer")    
        self.length = width
           

rl = Rectangle(length= 30, width=35)
print(rl.__dict__)
rl.area()
print(rl.__dict__)
rl._length = 70
print(rl.__dict__)
rl.area()

