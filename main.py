import random

from world import World


if __name__ == "__main__":
    world = World()
    country = random.choice(world.countries)
    while True:
        print("You are in {0}!".format(country))
        print("Neighbouring countries:")
        for c in country.neighbours:
            print(" - {0}: {1} km away".format(c, country.neighbours[c]))
        input()