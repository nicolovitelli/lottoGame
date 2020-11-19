import random
import lotto_lottery

class Wheel:
    def __init__(self, numbers):
        self.numbers = numbers

    def randomWheel(self):
        generated = []
        x = 0

        while x != self.numbers:
            generated.append(random.randint(1, 90))
            x = x + 1
            print("Numbers Generated:")
            for element in generated:
                print("{}".format(element))
