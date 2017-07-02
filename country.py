class Country:
    def __init__(self, name, stats):
        self.name = name
        self.neighbours = {}

    def mark_neighbour(self, country, distance=10):
        if is_neighbouring(country):
            return False

        self.ajorning[country] = distance
        return True

    def is_neighbouring(self, country):
        return country in self.neighbours
