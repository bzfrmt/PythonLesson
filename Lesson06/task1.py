import itertools
import time
class TrafficLight():
    __color="yellow"
    tracklist=["red","yellow","green","yellow"]
    lighttime={"yellow":2,"red":7,"green":10}
    def running(self):
        for light in itertools.cycle(self.tracklist):
            self.__color=light
            print (self.__color)
            time.sleep(int(self.lighttime[light]))

a=TrafficLight()
a.running()