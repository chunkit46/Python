# Assignment 7, Task 3
# Name: Chirasak Au Yeung
# Collaborators:
# Time Spent: 1hr


class DataFrame:
    def __init__(self):
        self.items = []

    def add(self, x):
        if type(x) == float or type(x) == int:
            self.items.append(x)
        elif type(x) == list or type(x) == tuple:
            for item in x:
                self.items.append(item)

    def mean(self):
        return sum(self.items) / len(self.items)

    def percentile(self, r):
        self.items.sort()
        position = r / 100 * len(self.items)
        return self.items[int(position)]

    def mode(self):
        counts = {}
        for item in self.items:
            if item in counts:
                counts[item] += 1
            else:
                counts[item] = 1

        max_count = 0
        mode = None
        for item, count in counts.items():
            if count > max_count:
                max_count = count
                mode = item

        return mode

    def sd(self):
        mean = self.mean()
        sum_of_squared_deviations = 0
        for item in self.items:
            sum_of_squared_deviations += (item - mean) ** 2
        variance = sum_of_squared_deviations / len(self.items)
        return variance ** 0.5