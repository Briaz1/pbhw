class Road:
    _length = float(input('Enter road length (meters): '))  # meters
    _width = float(input('Enter road width (meters): '))  # meters

    def asphalt_calc(self):
        asp_mass = 0.025  # tons
        asp_height = 5  # centimeters
        return f'You need {self._length * self._width * asp_height * asp_mass} tons of asphalt'


m = Road()
print(m.asphalt_calc())
