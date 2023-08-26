my_name= input("what is your name?")
my_age= int(input("what is your age?"))

print(f"my name is {my_name} and i am {my_age} years old")

first_number=int(input("inter a number"))
secound_number=int(input("inter a 2nd a number"))
operation= input("which operation would you like to use?")

if operation == "+":
    print(first_number+secound_number)
elif operation == "-":
    print(first_number-secound_number)
elif operation == "*":
    print(first_number*secound_number)
elif operation == "/":
    print(first_number/secound_number)
else:
    print('the operation is not valid')


bus_capacity= 25
people_in= int(input("how many people are in the bus now?"))
people_out= int(input("how many people want to enter?"))
emty_seats= bus_capacity-people_in

if emty_seats >= people_out:
        print("there is spece!")
else:
        print("the bus is full!")
