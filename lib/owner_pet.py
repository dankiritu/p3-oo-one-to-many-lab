class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []

    def pets(self):
        return self._pets

    def add_pet(self, pet):
        if isinstance(pet, Pet):
            self._pets.append(pet)
            pet.owner = self
        else:
            raise TypeError("Can only add Pet objects")

    def get_sorted_pets(self):
        return sorted(self._pets, key=lambda pet: pet.name)

class Pet:
    PET_TYPES = ['dog', 'cat', 'rodent', 'bird', 'reptile', 'exotic']
    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        if pet_type not in self.PET_TYPES:
            raise ValueError(f"Pet type must be one of: {', '.join(self.PET_TYPES)}")
        self.pet_type = pet_type
        self.owner = owner
        if owner:
            owner.add_pet(self)
        Pet.all.append(self)

# Clear the Pet.all list before running tests
Pet.all.clear()