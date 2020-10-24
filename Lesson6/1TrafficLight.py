from time import sleep, time


class TrafficLight:
    color = {'Red': 7, 'Yellow': 2, 'Green': 12}

    def running(self, work_time):
        start = time()
        while time() < start + work_time:
            for colors in self.color:
                print(colors)
                sleep(self.color.get(colors))


t = TrafficLight()
t.running(input("Enter (in sec) how long will traffic lights run: "))
