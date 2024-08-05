#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand = "Adidas", size = 9, condition = ""):
        self.brand = brand
        self.size = size
        self._condition = condition

    @property
    def size(self):
        return self._size 
    
    @size.setter
    def size(self, size):
        if isinstance(size, int):
            self._size = size
        else:
            print("size must be an integer")

    @property
    def condition(self):
        return self._condition 
    
    @condition.setter
    def condition(self, condition):
        self._condition = condition

    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"
