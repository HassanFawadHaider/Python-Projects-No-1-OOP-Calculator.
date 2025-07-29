# ==============================
#   CALCULATOR PROJECT
#   Basic + Advanced + Scientific
#   With Calculation History
# ==============================

import math as mt

# ==============================
# Base Calculator Class
# ==============================
class Calculator():
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    # Safely get first number (float)
    def getNum1(self):
        while True:
            try:
                self.num1 = float(input("Enter Number 1: "))
                return self.num1
            except:
                print("Invalid input! Please enter a valid number.")

    # Safely get second number (float)
    def getNum2(self):
        while True:
            try:
                self.num2 = float(input("Enter Number 2: "))
                return self.num2
            except:
                print("Invalid input! Please enter a valid number.")


# ==============================
# Basic Calculator (Add, Sub, Mul, Div)
# ==============================
class Basic_Calculator(Calculator):
    # Addition
    def Add(self):
        print("========Addition=========")
        self.Num1 = self.getNum1()
        self.Num2 = self.getNum2()
        self.Result = self.Num1 + self.Num2
        print(f"Result = {self.Result}")
        with open("D:\\fileX\\calculations.txt", "a") as file:
            file.write(f"Addition: {self.Num1} + {self.Num2} = {self.Result}\n")

    # Subtraction
    def Sub(self):
        print("========Subtraction=========")
        self.Num1 = self.getNum1()
        self.Num2 = self.getNum2()
        self.Result = self.Num1 - self.Num2
        print(f"Result = {self.Result}")
        with open("D:\\fileX\\calculations.txt", "a") as file:
            file.write(f"Subtraction: {self.Num1} - {self.Num2} = {self.Result}\n")

    # Multiplication
    def Multiply(self):
        print("=======Multiplication========")
        self.Num1 = self.getNum1()
        self.Num2 = self.getNum2()
        self.Result = self.Num1 * self.Num2
        print(f"Result = {self.Result}")
        with open("D:\\fileX\\calculations.txt", "a") as file:
            file.write(f"Multiplication: {self.Num1} × {self.Num2} = {self.Result}\n")

    # Division (with zero check)
    def Divide(self):
        print("=========Division===========")
        self.Num1 = self.getNum1()
        self.Num2 = self.getNum2()
        if self.Num2 == 0:
            print("Error: Division by zero is not allowed.")
            return
        self.Result = self.Num1 / self.Num2
        print(f"Result = {self.Result}")
        with open("D:\\fileX\\calculations.txt", "a") as file:
            file.write(f"Division: {self.Num1} ÷ {self.Num2} = {self.Result}\n")


# ==============================
# Advanced Calculator (Power, Modulo, etc.)
# ==============================
class Advance_Calculator(Calculator):
    # Power
    def Power(self):
        print("=======Power=========")
        self.Num1 = self.getNum1()
        self.Num2 = self.getNum2()
        self.Result = mt.pow(self.Num1, self.Num2)
        print(f"Result = {self.Result}")
        with open("D:\\fileX\\calculations.txt", "a") as file:
            file.write(f"Power: {self.Num1}^{self.Num2} = {self.Result}\n")

    # Modulus
    def Module(self):
        print("=======Modulus========")
        self.Num1 = self.getNum1()
        self.Num2 = self.getNum2()
        self.Result = self.Num1 % self.Num2
        print(f"Result = {self.Result}")
        with open("D:\\fileX\\calculations.txt", "a") as file:
            file.write(f"Modulus: {self.Num1} % {self.Num2} = {self.Result}\n")

    # Floor Division
    def FloorDivison(self):
        print("=========Floor Division===========")
        self.Num1 = self.getNum1()
        self.Num2 = self.getNum2()
        self.Result = self.Num1 // self.Num2
        print(f"Result = {self.Result}")
        with open("D:\\fileX\\calculations.txt", "a") as file:
            file.write(f"Floor Division: {self.Num1} // {self.Num2} = {self.Result}\n")

    # Square Root
    def sqrt(self):
        print("=========Square Root===========")
        self.number = self.getNum1()
        self.Result = mt.sqrt(self.number)
        print(f"Result = {self.Result}")
        with open("D:\\fileX\\calculations.txt", "a") as file:
            file.write(f"Square Root of {self.number} = {self.Result}\n")

    # Factorial
    def factorial(self):
        print("=========Factorial=========")
        self.number = self.getNum1()
        self.Result = mt.factorial(int(self.number))  # Factorial only for integers
        print(f"Result = {self.Result}")
        with open("D:\\fileX\\calculations.txt", "a") as file:
            file.write(f"Factorial of {self.number} = {self.Result}\n")


# ==============================
# Scientific Calculator (Trig + Logs)
# ==============================
class Scientific_Calculator(Calculator):
    # Trigonometric Functions
    def Trignometric_functionalities(self):
        while True:
            print("\n======Choose Trigonometric Operation======")
            print("1. Sin\n2. Cos\n3. Tan\n4. Cosec\n5. Sec\n6. Cot\n7. Exit")
            self.choose = input("Enter choice from 1-7: ")

            if self.choose in ["1", "2", "3", "4", "5", "6"]:
                self.choose_angle = input("Choose r or d (radian/degree): ")
                self.angle = float(input("Enter value of angle: "))
                if self.choose_angle == "d":  # Convert degrees to radians
                    self.angle = mt.radians(self.angle)

                # Perform calculation based on choice
                if self.choose == "1": self.Result = mt.sin(self.angle)
                elif self.choose == "2": self.Result = mt.cos(self.angle)
                elif self.choose == "3": self.Result = mt.tan(self.angle)
                elif self.choose == "4": self.Result = 1 / mt.sin(self.angle)
                elif self.choose == "5": self.Result = 1 / mt.cos(self.angle)
                elif self.choose == "6": self.Result = 1 / mt.tan(self.angle)

                print(f"Result = {self.Result}")
                with open("D:\\fileX\\calculations.txt", "a") as file:
                    file.write(f"Trig Result ({self.choose}): {self.Result}\n")

            elif self.choose == "7":
                print("Exited Trigonometry menu.")
                break
            else:
                print("Invalid choice! Please select between 1 to 7.")

    # Logarithms & Exponentials
    def Logrithm(self):
        while True:
            print("\n======Choose Logarithmic Operation======")
            print("1. Natural log (ln)\n2. Base 10 log\n3. Log with custom base\n4. Exponential (e^x)\n5. Exit")
            self.choose = int(input("Enter a choice (1-5): "))

            if self.choose == 1:
                self.number = float(input("Enter the number: "))
                self.Result = mt.log(self.number)
                print(f"Result = {self.Result}")
            elif self.choose == 2:
                self.number = float(input("Enter the number: "))
                self.Result = mt.log10(self.number)
                print(f"Result = {self.Result}")
            elif self.choose == 3:
                self.number = float(input("Enter the number: "))
                self.base = float(input("Enter the Base: "))
                self.Result = mt.log(self.number, self.base)
                print(f"Result = {self.Result}")
            elif self.choose == 4:
                self.number = float(input("Enter the number: "))
                self.Result = mt.exp(self.number)
                print(f"Result = {self.Result}")
            elif self.choose == 5:
                print("Exiting Logarithm menu.")
                break
            else:
                print("Invalid choice! Please choose between 1–5.")
                continue
            with open("D:\\fileX\\calculations.txt", "a") as file:
                file.write(f"Logarithm/Exponential Result: {self.Result}\n")

    # History Menu
    def Calculations_History(self):
        while True:
            print("\n1. View History\n2. Clear History\n3. Search History\n4. Back To Menu")
            self.choice = int(input("Enter a choice (1-4): "))

            if self.choice == 1:  # View
                with open("D:\\fileX\\calculations.txt", "r") as file:
                    self.content = file.read()
                    print(self.content if self.content.strip() else "History is empty.")
            elif self.choice == 2:  # Clear
                open("D:\\fileX\\calculations.txt", "w").close()
                print("History cleared successfully.")
            elif self.choice == 3:  # Search
                self.keyword = input("Enter a keyword to search: ")
                with open("D:\\fileX\\calculations.txt", "r") as file:
                    found = False
                    for line in file:
                        if self.keyword.lower() in line.lower():
                            print(line.strip())
                            found = True
                    if not found:
                        print("No match found.")
            elif self.choice == 4:
                break


# ==============================
# Combine All Classes
# ==============================
class All_Calculators(Basic_Calculator, Advance_Calculator, Scientific_Calculator):
    pass


# ==============================
# Main Menu Loop
# ==============================
a1 = All_Calculators(0.0, 0.0)
while True:
    print("\n======Choose Operation======")
    print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Power\n6.Modulus\n7.Floor Division\n8.Square Root\n9.Trigonometry\n10.Logarithm\n11.History\n12.Exit")
    choice = input("Enter Choice (1-12): ")

    operations = {
        "1": a1.Add, "2": a1.Sub, "3": a1.Multiply, "4": a1.Divide,
        "5": a1.Power, "6": a1.Module, "7": a1.FloorDivison,
        "8": a1.sqrt, "9": a1.Trignometric_functionalities,
        "10": a1.Logrithm, "11": a1.Calculations_History
    }

    if choice == "12":
        print("Exiting Calculator. Goodbye!")
        break
    elif choice in operations:
        operations[choice]()
    else:
        print("Invalid Input.")
