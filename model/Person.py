
class Person:
    def __init__(self,first_name,last_name,age,id):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.id=id
        self.pets_list=[]

    def print_attributes(self):
        print(self.__dict__)

        # Support with methods the ability to add new animal to the person’s animal array
        # and remove existing animal from that array.
        # Keep in mind to add validations if needed.
        # Check your implementation in the main thread

    def add_animal(self,animal):
        self.pets_list.append(animal)

    def remove_animal(self, animal):
        if animal in self.pets_list:
            self.pets_list.remove(animal)
        else:
            print(f"this pet index isn't exist in {self.first_name}'s pets list")