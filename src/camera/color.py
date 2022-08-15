class Color:
    def __init__(self, r: float, g: float, b: float, a: float):
        self.r = r
        self.g = g
        self.b = b
        self.a = a

    def __str__(self):
        return "Color(r: {0}, g: {1}, b: {2}, a: {3})".format(
            self.r, self.g, self.b, self.a
        )
