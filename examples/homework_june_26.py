

# Homework
from area_service import Area_Service
from paint_service import Paint_Service


rectangle_object = {}
rectangle_object["One"] = [34, 12, "red"] # [length, width, colour]
rectangle_object["Two"] = [45, 34, "green"]
rectangle_object["Three"] = [56, 43, "yellow"]
rectangle_object["Four"] = [12, 12, "pink"]
rectangle_object["Five"] = [15, 29, "orange"]

print(len(rectangle_object))

list_of_keys = list(rectangle_object.keys())
print(list_of_keys[0])
print(list_of_keys)

counter = 0

while counter < len(list_of_keys):
    key = list_of_keys[counter]
    print(key)
    value = rectangle_object[key]
    radius = value[0]
    colour = value[1]
    rectangle_area = area_svc_obj.area_reactangle(width = width,length=length)
    paint_task_resp = paint_svc_obj.paint_(area=rectangle_area, color=colour)
    print(paint_task_resp)


    # print("Key is {} and radius is {} and colour is {}".format(key,radius,colour))
    counter = counter + 1




# Service class that controls a automobile
# park
# drive forward
# drive in reverse
# breaks
# Power On/off
# play music
# blow horn
# A/C on or off
# headlight on/off


class Animal:
    planet = "Earth"
    def eat_food(self):
        return "Eat Vegetarian Food"

    def make_sound(self):
        return "make sound"

    def sleep_night(self):
        return "sleep at night"


class Tiger(Animal):

    def type(self):
        return "I am a type of a Tiger"

    def eat_food(self):
        return "Eat Hunted-Animal Food"

class White_Tiger(Tiger):

    def type(self):
        return "I am a type of a White Tiger"

my_special_pet_white_tiger = White_Tiger()

print(my_special_pet_white_tiger.type())
print(my_special_pet_white_tiger.eat_food())
print(my_special_pet_white_tiger.planet)

print(" ")


class Dog(Animal):

    def type(self):
        return "I am a type of a Dog"

my_special_pet_tiger = Tiger()
my_special_pet_dog = Dog()

print(my_special_pet_tiger.type())
print(my_special_pet_tiger.eat_food())
print(my_special_pet_tiger.planet)

print(" ")

print(my_special_pet_dog.type())
print(my_special_pet_dog.eat_food())
print(my_special_pet_dog.planet)
