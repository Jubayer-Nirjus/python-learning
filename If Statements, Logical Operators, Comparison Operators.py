
# Example 1: Basic If Statement

# a = int(input("Enter a number: ")) 

# if a > 10:
#     print("Number is Greater than 10") 
# elif a < 10 and a > 0: 
#      print("Number is Not Greater than 10")
# elif a < 0: 
#      print("Please , Enter a positive Number")
# else: 
#      print("Number is Invalid")

# print("Programme is DONE!") 

# Ex-2: 

# a = int(input("Enter a number: ")) 

# if a % 2 == 0:
#      print(f"{a} is a Even Number") 
# else:
#      print(f"{a} ia a Odd Number")
     
# Ex- 3 

# mark = int(input("Enter your mark: ")) 

# if mark >= 80 and mark <=100: 
#     print("Your grade is: A+")
# elif mark >= 70 and mark < 80: 
#     print("Your grade is: A") 
# elif mark >= 60 and mark < 70: 
#     print("Your grade is: A-") 
# elif mark >= 50 and mark < 60: 
#     print("Your grade is: B") 
# elif mark >= 40 and mark < 50: 
#     print("Your grade is C") 
# elif mark < 40: 
#     print("You Failed, Sona") 
# else: 
#     print("Please Enter valid number") 

# Ex- 4 

# age = int(input("Enter your Age: ")) 


# if age >= 18: 
#     driving_lin = input("Are you have Driving Lisence(yes/no): ").lower()
#     if driving_lin == "yes": 
#         print("You are allow to Drive") 
#     else: 
#         print("Please issue your Driving lisence first") 
# elif age <= 18 and age > 0: 
#     print("You are underage to Drive") 
# else: 
#     print("Please, Enter valid Age") 


# Ex- 5 

# age = int(input("Enter your age: ")) 

# if age >= 21: 
#     education = input("Are you complete your Graduation ?(Yes/No)").lower() 
#     if education == "yes": 
#         print("Congratulation !! You are Eligible for the Job") 
#     else: 
#         print("Complete your Graduation First") 
# if age < 21 and age !=0 : 
#     experience = input("Are you have minimum 5 year's work experience ?(Yes/No)").lower() 
#     if experience == "yes": 
#         print("You are eligible") 
#     else: 
#         print("You are not Eligible") 

# shortcut :-  

# age = int(input("Enter your age: ")) 
# education = input("Enter your education(highschool/graduate/college/master): ").lower() 
# experence = int(input("Enter your yerars of experience: ")) 

# if (age >= 21 and education in ["graduate", "master"]) or experence >= 5: 
#     print("You are eligible for the Job !✅ ") 
#     if experence < 5: 
#         print("-You are eligible by education and age") 
#     elif age < 21 and experence >= 5 : 
#         print("- You are eligible by work experience ! ")
# else: 
#     print("You are not eligible")

# # Example 6: Comparison Operators 

# a = int(input("Enter first number: ")) 
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: ")) 

# print("\nComparison Result---") 

# if a > b : 
#     print(f"{a} is Greater than {b}") 
# elif a < b : 
#     print(f"{b} is greater than {a}") 
# else: 
#     print(f"{a} and {b} are equal") 

# if b > c : 
#     print(f"{b} is greater than {c}") 
# elif b < c : 
#     print(f"{c} is greater than {b}") 
# else : 
#     print (f"{b} and {c} are equal") 

# if a >= b and a >= c: 
#     print(f"{a} is the largest number") 
# elif b >= a and b >= c: 
#     print(f"{b} is the largest number") 
# else: 
#     print(f"{c} is the largest number") 

# if a == b == c : 
#      print("All numbers are equal")
# elif a == b or a == c or b == c: 
#     print("Two numbers ar Equal") 
# else: 
#     print("All number are deffents") 

# # Example 7: Multiple Conditions with 'and'

# math = int(input("Enter your math's number: ")) 
# english = int(input("Enter your english's number: ")) 
# science = int(input("Enter your science's number: ")) 

# total = (math + english + science) 
# percentage = (f"{total/3:.2f}")

# if math > 100 or english > 100 or science > 100:
#     print("Invalid number")
# elif math >= 40 and english >= 40 and science >= 40:
#     print(f"You are passed and your percentage is {percentage}%")
#     if total >= 200:
#         print("You got good total marks ")
#     if science >= 60: 
#         print("You make excellent results with great mark in Science ") 
# elif math < 40 or science < 40 or english < 40: 
#     print("You are failed at least one subject") 

# Example 8: Using 'or' for Multiple Options 


    



