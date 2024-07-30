import random

class Teenda:
    def __init__(self, values):
        self.values = values

    def is_valid(self):
        if len(self.values) != 3 and len(self.values) != 5:
            return False
        if len(self.values) == 3 and (self.values[1] <= self.values[0] or self.values[1] <= self.values[2]):
            return False
        if len(self.values) == 5 and (self.values[2] <= self.values[0] or self.values[2] <= self.values[4] or self.values[1] <= self.values[3]):
            return False
        return True

    def mutate(self):
        if len(self.values) == 3 and random.random() < 0.5:
            avg1 = (self.values[0] + self.values[1]) // 2
            avg2 = (self.values[1] + self.values[2]) // 2
            self.values.insert(1, avg1)
            self.values.insert(3, avg2)

        elif len(self.values) == 5 and random.random() < 0.5:
            mid = self.values[2] // 2
            teenda1 = Teenda([self.values[0], mid, self.values[1]])
            teenda2 = Teenda([self.values[3], mid, self.values[4]])
            if teenda1.is_valid() and teenda2.is_valid():
                return teenda1, teenda2
            else:
                return self
        return self

    def display(self):
        print("<", end="")
        for i in range(len(self.values)):
            print(self.values[i], end="")
            if i < len(self.values) - 1:
                print(", ", end="")
        print(">", end="")

teenda1 = Teenda([4, 5, 2])
teenda2 = Teenda([23, 35, 40, 30, 20])


teenda1 = teenda1.mutate()
teenda2 = teenda2.mutate()
teenda1.display()
print()
teenda2.display()
print()





