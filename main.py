#Name: Evan Thong
#Team Members: Jennifer Jiang and Chen-Ha Ma

def addition():
    num1 = input("What is the first number you want to add? ")
    num2 = input("What is the second number you want to add? ")
    ans = int(num1) + int(num2)
    print(ans)

def subtraction():
    num_1 = input("What is the first number you want to subtract? ")
    num_2 = input("What is the second number you want to subtract? ")
    answers = int(num_1) - int(num_2)
    print(answers)

user_input = input("Do you want to do addition or subtraction: ")

if user_input == "addition":
    addition()

elif user_input == "subtraction":
    subtraction()

