class Jar:
    def __init__(self, capacity=12):
        if type(capacity) == int and capacity > 0:
            self._capacity = capacity
            self._size = 0
        else:
            raise ValueError("Invalid capacity")

    def __str__(self):
        return(f"{self.size * '🍪'}")

    def deposit(self, n):
        if self.size + n <= self.capacity:
            self.size += n
        else:
            raise ValueError("Over capacity")


    def withdraw(self, n):
        if self.size >= n:
            self.size -= n
        else:
            raise ValueError("Over size")

    @property
    def capacity(self):
        return self._capacity


    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        self._size = size
