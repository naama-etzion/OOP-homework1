from model.Animal import Animal
from model.Person import Person
from model.Rectangle import Rectangle


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

if __name__ == '__main__':
    print_hi('PyCharm')

#EX 1

first_student=Person("Shahar","Etzion",31,"44444")
second_student=Person("Elad","Etzion",29,"44444")
third_student=Person("Naama","Etzion",22,"22343535")

print(type(first_student))
print(type(second_student))
print(type(third_student))

#first student
print(getattr(first_student,"first_name"))
setattr(first_student,"last_name","Fremder")
print(first_student.__dict__)
print(getattr(first_student,"age"))
setattr(first_student,"age",32)
print(getattr(first_student,"age"))

#second student
second_student.age=30
print(second_student.age)

#EX2
first_animal=Animal("ztupa","dog","brown",10,True)
first_student.add_animal(first_animal)
print(first_student.__dict__)

first_student.remove_animal(first_animal)
print(first_student.__dict__)

first_student.remove_animal(first_animal)

my_rectangle=Rectangle(4,5)
print(my_rectangle.get_area())