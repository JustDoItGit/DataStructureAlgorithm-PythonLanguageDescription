class Assoc:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __lt__(self, other):
        return self.key < other.key

    def __le__(self, other):
        # return self.key < other.key or self.key == other.key
        return self.key <= other.key

    def __str__(self):
        return 'Assoc({0}{0})'.format(self.key, self.value)
