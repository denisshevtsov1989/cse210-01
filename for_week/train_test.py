class House():
    """Описание дома"""

    def __init__(self, street, number):
        """свойства дома"""
        self.street = street
        self.number = number
        self.age = 0

    def build(self):
        """строит дом"""
        print("Дом на улице " + self.street +
              " под номером " + str(self.number) + " построен.")

    def age_of_house(self, year):
        """Возраст дома"""
        self.age += year


class ProspectHouse(House):
    """Дома на проспекте"""

    def __init__(self, prospect, number):
        super().__init__(self, number)
        self.prospect = prospect


PrHouse = ProspectHouse("Ленина", 5)
print(PrHouse.prospect)
