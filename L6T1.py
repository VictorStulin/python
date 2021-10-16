import time


class TrafficLight:

    def __init__(self, color):
        self.__color = color

    def running(self):
        pause = (7, 2, 5)
        for i in range(3):
            print(self.__color[i])
            time.sleep(pause[i])

    def test(self):
        if self.__color != ['red', 'yellow', 'green']:
            print('Wrong Order')
            quit()


my_traffic_light_1 = TrafficLight(['red', 'yellow', 'green'])
my_traffic_light_2 = TrafficLight(['red', 'yellow', 'green', 'blue'])

my_traffic_light_1.test()
my_traffic_light_1.running()

my_traffic_light_2.test()
my_traffic_light_2.running()
