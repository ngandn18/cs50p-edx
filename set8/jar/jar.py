class Jar:
    def __init__(self, size = 0, capacity=12):
        if type(capacity) != int or capacity < 0:
            raise ValueError("Invalid capacity")
        self._capacity = capacity
        if type(size) != int or size < 0:
            raise ValueError("Invalid size")
        self._size = size


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
