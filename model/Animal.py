

#

class Animal:
    def __init__(self,pet_name,pet_type,pet_color,pet_weight,has_home):
        self.pet_name=pet_name
        self.pet_type=pet_type
        self.pet_color=pet_color
        self.pet_weight=pet_weight
        self.has_home=has_home

    def print_attributes(self):
        print(f"pet name: {self.pet_name}, pet type: {self.pet_type}, pet color: {self.pet_color}, pet weight: {self.pet_weight},has home: {self.has_home}")

