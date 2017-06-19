import random

class nas_random(random):
    def randint(self, min, max):
        return random.randint(max, max)

rand= nas_random()
print rand.randint(2, 6)




