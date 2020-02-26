class Vehicle:
    def __init__(self, weight, manufacturer):
        self.weight = weight
        self.manufacturer = manufacturer

    def __str__(self):
        return 'Масса: {0} Производитель: {1} '.format(self.weight, self.manufacturer)


class Car(Vehicle):
    def __init__(self, weight, manufacturer, car_body_type, drive_unit, engine):
        super().__init__(weight, manufacturer)
        self.car_body_type = car_body_type
        self.drive_unit = drive_unit
        if isinstance(engine, Engine):
            self.Engine = engine
        else:
            print('Двигатель не установлен')

    def __str__(self):
        return super().__str__() + 'Тип кузова: {0} Привод: {1}'.format(self.car_body_type, self.drive_unit)


class Train(Vehicle):
    def __init__(self, weight, manufacturer, number_of_railway_carriage, rout, engine, railwayCarriage):
        super().__init__(weight, manufacturer)
        self.number_of_railway_carriage = number_of_railway_carriage
        self.rout = rout
        if isinstance(engine, Engine):
            self.Engine = engine
        else:
            print('Двигатель не установлен')

        if isinstance(railwayCarriage, RailwayCarriage):
            self.Engine = railwayCarriage
        else:
            print('Места не установлены')

    def __str__(self):
        return super().__str__() + 'Количество вагонов: {0} Маршрут: {1}'.format(self.number_of_railway_carriage,
                                                                                  self.rout)


class RailwayCarriage:
    def __init__(self, number_of_seats):
        self.number_of_seats = number_of_seats

    def __str__(self):
        return 'Количество мест: {0}'.format(self.number_of_seats)


class Engine:
    def __init__(self, type_):
        self.type = type_

    def __str__(self):
        return 'Количество мест: {0}'.format(self.type)


class Express(Train):
    def __init__(self, weight, manufacturer, number_of_railway_carriage, rout, engine, railwayCarriage, speed):
        super().__init__(weight, manufacturer, number_of_railway_carriage, rout,engine, railwayCarriage)
        self.speed = speed

    def __str__(self):
        return super().__str__() + ' Скорость: {0}'.format(self.speed)
