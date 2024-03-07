from math import sqrt

class Vectors:
    def __init__(self, *args):
        self.arguments = args

    def show(self):
        return f"Vector{self.arguments}"

    def dimension(self):
        return len(self.arguments)

    def length(self):
        return round(sqrt(sum(arg**2 for arg in self.arguments)), 3)

    def middle(self):
        return round(sum(self.arguments) / len(self.arguments), 3)

    def min(self):
        return min(self.arguments)

    def max(self):
        return max(self.arguments)

if __name__ == '__main__':
    v1 = Vectors(2, 7)
    print(v1.show())
    print(v1.dimension())
    print(v1.length())
    print(v1.middle())
    print(v1.min())
    print(v1.max())
