from time import sleep, time


class TrafficLight:
    color = {'Red': 7, 'Yellow': 2, 'Green': 10}

    def running(self, work_time):
        start = time()
        m = 0
        while time() < start + work_time:
            for colors in self.color:
                m += 1
                if time() > start + work_time:
                    break
                print(f"{m}: {colors}")
                sleep(self.color.get(colors))


while True:
    try:
        tr = TrafficLight()
        tr.running(int(input("How time(sec) traffic light must work?: ")))
    except ValueError:
        continue
