
class Road:
    def __init__(self, leght, width):
        self._road_leght = leght
        self._road_width = width

    def mass_road(self):
        result = self._road_leght * self._road_width * 25 * 5
        print(result, 't')

one_road = Road(20, 5000)
one_road.mass_road()

print(one_road._road_leght)
