# from dotenv import load_dotenv
# import os
# load_dotenv()

# secret_key=os.getenv('SECRET_KEY')
# print('secret key',secret_key)

# square = lambda x: x**2
# print(square(5))
# age =17
# status= "Adult" if age>=18 else "Child"
# print(status)

# numbers=[1,2,3,4,5]
# squares=[i*i for i in numbers]
# print(squares)

# List comprehension

# dic={x:x*2 for x in range(5)}

# print(dic)

try:
    a=int(input("Enter a number a: "))
    b=int(input("Enter numbe b"))

    result=a/b
except ValueError:
    print("Pleasse enter valid number")
except ZeroDivisionError:
    print("infinite")
except Exception as e:
    print(f"{e}")

else:
    print('result', result)    