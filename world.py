import random
import re

from country import Country


DEFAULT_STATS = {
    "space": 5,  # building count max
    "population": 5,  # self explanatory
    "max_neighbours": 3,  # max countries that border this one
    "min_neighbours": 1,  # min countries that border this one
    "has_water": -1  # 1 = yes, 0 = no, if 1 then there is a coast/river/lake
}

class World:
    def __init__(self):
        self.countries = self.load_countries()
        for country in self.countries:
            options = list(self.countries)
            options.remove(country)
            random.shuffle(options)
            while len(country.neighbours) < country.neighbour_count:
                country.mark_neighbour(options.pop())

    def load_countries(self):
        countries = {}

        with open("namepool.txt") as namepool_file:
            for line in namepool_file.read().split("\n"):
                if line:
                    found = re.match("(.*?)\s*\[(.*?)\]", line)
                    if found is None:  # No stats given:
                        countries[line] = dict(DEFAULT_STATS)  # Create copy of DEFAULT_STATS
                        countries[line]["has_water"] = random.choice([0, 1])
                    else:
                        name = found[1]
                        stats = found[2]

                        stats = {}
                        for stat in found[2].split(","):
                            key, value = stat.split(":")
                            key = key.lstrip().rstrip()
                            value = int(value)
                            if key not in DEFAULT_STATS:
                                raise ValueError("Stat '{0}' in country '{1}' not recognised!".format(key, name))
                            stats[key] = value

                        for default_stat in DEFAULT_STATS:
                            if default_stat not in stats:
                                stats[default_stat] = DEFAULT_STATS[default_stat]
                                if default_stat == "has_water":
                                    stats[default_stat] = random.choice([0, 1])

                        countries[found[1]] = stats

        countries_ret = []
        for country in countries:
            countries[country]["neighbours"] = random.randint(countries[country]["min_neighbours"], countries[country]["max_neighbours"])
            countries_ret.append(Country(country, countries[country]))

        return countries_ret
