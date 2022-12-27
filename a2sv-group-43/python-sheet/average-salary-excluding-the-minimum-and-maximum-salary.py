class Solution:
    def average(self, salaries: list[int]) -> float:
        smallest = salaries[0]
        largest = salaries[0]
        total = 0

        for salary in salaries:
            if (smallest > salary):
                smallest = salary
            if (largest < salary):
                largest = salary
            total += salary

        average = (total - smallest - largest) / (len(salaries) - 2)
        return average
