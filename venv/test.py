import copy
class Atomic:
    def __init__(self, data, deep = False):
        self.data = data
        self.deep = deep
        self.tmp_data = copy.deepcopy(self.data) if self.deep else copy.copy(self.data)


    def __enter__(self):
            return self.tmp_data


    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_val:
            return True
        else:
            if isinstance(self.data, list):
                self.data[:] = self.tmp_data
            elif isinstance(self.data, dict|set):
                self.data.clear()
                self.data.update(self.tmp_data)
        return False


numbers = {1, 2, 3, 4, 5}

with Atomic(numbers) as atomic:
    atomic.add(6)
    atomic.append(7)           # добавление элемента с помощью несуществующего метода

print(sorted(numbers))

with Atomic(numbers) as atomic:
    atomic.add(6)

print(sorted(numbers))
