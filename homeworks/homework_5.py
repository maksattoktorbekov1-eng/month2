class Distance:
    _units_to_meters = {
        'mm': 0.001,
        'cm': 0.01,
        'm': 1,
        'km': 1000
    }

    def __init__(self, value, unit='m'):
        if unit not in self._units_to_meters:
            raise ValueError(f"Недопустимая единица измерения: {unit}")
        self.value = value
        self.unit = unit

    def __str__(self):
        return f"{self.value} {self.unit}"

    def to_meters(self):

        return self.value * self._units_to_meters[self.unit]

    def _from_meters(self, meters, target_unit):

        return meters / self._units_to_meters[target_unit]

    def __add__(self, other):
        if not isinstance(other, Distance):
            raise TypeError("Можно складывать только объекты Distance")
        total_meters = self.to_meters() + other.to_meters()
        new_value = self._from_meters(total_meters, self.unit)
        return Distance(new_value, self.unit)

    def __sub__(self, other):
        if not isinstance(other, Distance):
            raise TypeError("Можно вычитать только объекты Distance")
        diff_meters = self.to_meters() - other.to_meters()
        if diff_meters < 0:
            raise ValueError("Результат вычитания не может быть отрицательным")
        new_value = self._from_meters(diff_meters, self.unit)
        return Distance(new_value, self.unit)

    # доп задание
    def __eq__(self, other):
        return self.to_meters() == other.to_meters()

    def __lt__(self, other):
        return self.to_meters() < other.to_meters()

    def __le__(self, other):
        return self.to_meters() <= other.to_meters()

    def __gt__(self, other):
        return self.to_meters() > other.to_meters()

    def __ge__(self, other):
        return self.to_meters() >= other.to_meters()


# ===== ТЕСТЫ =====
if __name__ == "__main__":
    d1 = Distance(100, 'm')
    d2 = Distance(2, 'km')
    d3 = Distance(50, 'cm')

    print("d1:", d1)
    print("d2:", d2)
    print("d3:", d3)

    print("\nСложение:")
    print("d1 + d2 =", d1 + d2)

    print("\nВычитание:")
    print("d2 - d1 =", d2 - d1)

    print("\nСравнение:")
    print("d1 < d2:", d1 < d2)
    print("d2 > d3:", d2 > d3)
    print("d1 == Distance(100, 'm'):", d1 == Distance(100, 'm'))

    try:
        print("d1 - d2 =", d1 - d2)
    except ValueError as e:
        print("Ошибка:", e)
