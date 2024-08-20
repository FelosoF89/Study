class ReversedSequence:
    def __init__(self, item):
        self.item = item

    def __getitem__(self, key):
        return list(reversed(self.item))[key]

    def __len__(self):
        return len(self.item)

numbers = [1, 2, 3, 4, 5]
reversed_numbers = ReversedSequence(numbers)
print(len(reversed_numbers))

numbers.append(6)
numbers.append(7)
print(len(reversed_numbers))
print()