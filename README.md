How It Works
Menu‑Driven Interface:

Displays a main menu with numbered operations.

Sub‑menus for Trigonometry, Logarithms, and History.

File Handling:

All results are saved to D:\fileX\calculations.txt.

Users can view, search, or clear their calculation history.

Error Handling:

Invalid inputs are caught with try‑except.

Graceful handling for empty files, invalid options, and unsupported entries.

Installation & Setup
Clone the Repository:

bash
Copy
Edit
git clone https://github.com/yourusername/multi-functional-calculator.git
Run the Program:

bash
Copy
Edit
python calculator.py
Ensure the directory exists for history:
Create D:\fileX\ (or update the file path in code if needed).

Example Usage
text
Copy
Edit
======Choose Operation======
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Power
6. Modulus
7. Floor Division
8. Square Root
9. Trigonometry
10. Logarithms
11. History
12. Exit

Enter choice: 1
Enter Number 1: 15
Enter Number 2: 5
Result = 20.0
Trigonometry Example:

text
Copy
Edit
======Choose Trigonometric Operation======
1. Sin
2. Cos
3. Tan
...
Enter choice: 1
Choose r or d (radian/degree): d
Enter value of angle in degrees: 30
Result = 0.5
History Management
View History – Displays past calculations.

Clear History – Erases all entries.

Search History – Enter a keyword (e.g., "sin") to find matching results.

Future Enhancements
Graphical User Interface (GUI): Using Tkinter or PyQt.

Complex Numbers Support.

Unit Conversion & Scientific Constants.

Export History as PDF or CSV.

Why This Project?
This project is built for beginners to practice:

Object‑Oriented Programming (OOP)

Menu‑driven program design

Error handling

File operations

It is designed as a learning‑oriented project but structured enough to serve as a base for more advanced calculators
