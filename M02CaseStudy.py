# Daniel Bierman
# M02CaseStudy.py
# This program will ask the user to input last name, first name, and GPA of a student which will determine if the
# student has made the Dean's list or Honor Roll. 

last_name = ""
first_name = ""
gpa = 0.0

while last_name != "ZZZ":
    last_name = input("Please enter student's last name or 'ZZZ' to quit: ")
    if last_name == "ZZZ":
        break
    first_name = input("Please enter student's first name: ")
    gpa = float(input(f"What is {first_name} {last_name}'s GPA "))
    
    if gpa >= 3.5:
        print(f"{first_name} {last_name} has made the Dean's List!")
    elif gpa >= 3.25 and gpa < 3.5:
        print (f"{first_name} {last_name} has made the Honor Roll!")
    else: 
        print(f"{first_name} {last_name} did not make the Dean's list or Honor Roll.")
    
    