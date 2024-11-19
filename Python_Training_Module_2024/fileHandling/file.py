
# f=open('a.txt', 'r')
# print(f.read())
# f.close()

# f=open('a.txt', 'r')
# print(f.readline())
# f=open('a.txt', 'r')
# print(f.readline())
# print(f.readline())

# f.close()


# class Dog:
#     def __init__(self, name, age):
#         self.name= name
#         self.age = age
    
#     def bark(self):
#         return f"{self.name}"

# my_dog= Dog("buddy", 3)
# print(my_dog.bark())


def greet_decorator(func):
    def wrapper():
        print("Hello1")
        func()
        print("Hello2")
    return wrapper

@greet_decorator
def say_hello():
    print("Good morning")

say_hello()

