import random
from enum import Enum

CarType = Enum('CarType', 'subcompact compact suv')


class Car:
    pool = dict()

    def __new__(cls, car_type):
        obj = cls.pool.get(car_type, None)
        if not obj:
            obj = object.__new__(cls)
            cls.pool[car_type] = obj
            obj.car_type = car_type
        return obj

    def render(self, color, x, y):
        type = self.car_type
        msg = f'render a car of type {type} and color {color} at ({x}, {y})'
        print(msg)


def main():
    rnd = random.Random()
    # age_min, age_max = 1, 30 # in years
    colors = 'white black silver gray red blue brown beige yellow green'.split()
    min_point, max_point = 0, 100
    car_counter = 0
    used_places = []

    for _ in range(10):
        c1 = Car(CarType.subcompact)
        x=rnd.randint(min_point, max_point)
        y=rnd.randint(min_point, max_point)
        while [x, y] in used_places:
            x = rnd.randint(min_point, max_point)
            y = rnd.randint(min_point, max_point)
        used_places.append([x, y])
        c1.render(random.choice(colors), x, y)
        car_counter += 1

    for _ in range(3):
        c2 = Car(CarType.compact)
        x = rnd.randint(min_point, max_point)
        y = rnd.randint(min_point, max_point)
        while [x, y] in used_places:
            x = rnd.randint(min_point, max_point)
            y = rnd.randint(min_point, max_point)
        used_places.append([x, y])
        c2.render(random.choice(colors), x, y)
        car_counter += 1

    for _ in range(5):
        c3 = Car(CarType.suv)
        x = rnd.randint(min_point, max_point)
        y = rnd.randint(min_point, max_point)
        while [x, y] in used_places:
            x = rnd.randint(min_point, max_point)
            y = rnd.randint(min_point, max_point)
        used_places.append([x, y])
        c3.render(random.choice(colors), x, y)
        car_counter += 1

    print(f'cars rendered: {car_counter}')
    print(f'cars actually created: {len(Car.pool)}')

    c4 = Car(CarType.subcompact)
    c5 = Car(CarType.subcompact)
    c6 = Car(CarType.suv)
    print(f'{id(c4)} == {id(c5)}? {id(c4) == id(c5)}')
    print(f'{id(c5)} == {id(c6)}? {id(c5) == id(c6)}')

    print(f'Lista zaj??tych miejsc: {used_places}')

if __name__ == '__main__':
    main()
