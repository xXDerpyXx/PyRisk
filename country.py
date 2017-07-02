class Country:
    def __init__(self, name, stats):
        self.name = name

        self.has_water = bool(stats["has_water"])
        self.space = stats["space"]
        self.population = stats["population"]
        self.neighbour_count = stats["neighbours"]

        self.neighbours = {}

    def __repr__(self):
        return "<Country '{0}' object at 0x{1}>".format(self.name, id(self))
    def __str__(self):
        return self.name

    def mark_neighbour(self, country, distance=10):
        if self.is_neighbouring(country):
            return False

        self.neighbours[country] = distance
        return True

    def unmark_neighbour(self, country):
        if not self.is_neighbouring(country):
            return False

        del self.neighbours[country]
        return True

    def is_neighbouring(self, country):
        return country in self.neighbours
