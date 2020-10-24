from time import sleep


class TrafficLight:
    _color = {'Red': 7, 'Yellow': 2, 'Green': 12}

    def running(self):
        while True:
            for colors in self._color:
                print(colors)
                sleep(self._color.get(colors))


TrafficLight().running()


# from time import sleep, time
#
#
# class TrafficLight:
#     _color = {'Red': 7, 'Yellow': 2, 'Green': 12}
#
#     def running(self, work_time):
#         start = time()
#         while time() < start + work_time:
#             for colors in self._color:
#                 print(colors)
#                 sleep(self._color.get(colors))
#
#
# t = TrafficLight()
# t.running(float(input("Enter (in sec) how long will traffic lights run: ")))
