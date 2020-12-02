import random


class NumbersGenerator:
    def __init__(self, num_gen_amount):
        self.generated_numbers = []
        self.numGenerators(num_gen_amount)

    def numGenerators(self, num_gen_amount):
        self.generated_numbers = []
        while len(self.generated_numbers) < num_gen_amount:
            number = random.randint(1, 90)
            if number not in self.generated_numbers:
                self.generated_numbers.append(number)
