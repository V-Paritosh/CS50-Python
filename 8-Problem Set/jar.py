class Jar:
  def __init__(self, capacity=12):
    if capacity < 0:
      raise ValueError("Negative Capacity")
    self._capacity = capacity
    self._size = 0

  def __str__(self):
    str = ""
    for _ in range(self._size):
      str += "🍪"
    return str

  def deposit(self, n):
    if (n + self._size) > self._capacity:
      raise ValueError("Jar Full")
    self._size += n

  def withdraw(self, n):
    if (self._size - n) < 0:
      raise ValueError("Jar Empty")
    self._size -= n

  @property
  def capacity(self):
    return self._capacity

  @property
  def size(self):
    return self._size
