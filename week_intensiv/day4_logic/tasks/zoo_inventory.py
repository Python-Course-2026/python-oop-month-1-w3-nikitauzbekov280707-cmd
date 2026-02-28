class Animal:
    """Класс животного"""
    def __init__(self, species: str, food_per_day: float):
        self.species = species
        self.food_per_day = food_per_day

class ZooInventory:
    """
    ЗАДАЧА: Учет животных и их пропитания.
    1. calculate_monthly_food(): возвращает суммарное количество еды
       для всех животных в списке self.animals на 30 дней.
    2. count_species(species): возвращает количество животных конкретного вида.
    """
    def __init__(self):
        self.animals = []

    def add_animal(self, animal: Animal):
        self.animals.append(animal)

    def calculate_monthly_food(self):
        return 30*sum([animal.food_per_day for animal in self.animals])

    def count_species(self, species: str):
        species_animal = []
        for animal in self.animals:
            if animal.species == species:
                species_animal.append(animal)
        return len(species_animal)