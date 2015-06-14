__author__ = 'ceremcem'

from aktos_dcs import Actor,  ProxyActor, sleep, joinall
from aktos_dcs.Messages import *


class Ponger(Actor):
    def handle_PongMessage(self, msg):
        print "Pong got ping message:", msg.text
        sleep(5)
        self.send(PingMessage(text="Hello pinger!"))

if __name__ == "__main__":
    ProxyActor()
    ponger = Ponger()
    ponger.send(PingMessage(text="startup message from ponger..."))
    ponger.join()
