
# # Example 1: Variable Declaration & Print

# name = "Nirjus" 
# age = 25 
# height = 5.6 

# print("Name:", name) 
# print("Age:", age) 
# print("Height:", height) 

# # Example 2: Type Checking with type()

# a = 10      #int 
# b = 1.23    #float 
# c = "Hello"  #str 
# d = True    #bool 
# e = None #None type 
# f = [1, 2, 3]  #list 
# g = (1, 2, 3) #tuple 
# h = {"name": "Nirjus"} #dict 
# i = {1, 2, 3}

# print(type(a),type(b),type(c),type(d), type(e), type(f), type(g), type(h),type(i)) 


# # Example 3: Dynamic Typing in Action

# x = 100 
# print("x =", x, "-", type(x)) 
# x = 100.2
# print("x =", x, "-", type(x)) 
# x = "100"
# print("x =", x, "-", type(x)) 
# x = True 
# print("x =", x, "-", type(x)) 
# x = [1,2,3]
# print("x =", x, "-", type(x)) 

# # Example 4: Type Conversion (Casting) 

# str_num = "123" 
# int_num = int(str_num) 
# print(f'"{str_num}" ({type(str_num)}) - {int_num} ({type(int_num)})') 

# float_num = 3.23 
# int_num_f = int(float_num) 
# print(f'"{float_num}" ({type(float_num)}) - {int_num_f} ({type(int_num_f)})') 

# int_num_s = 456 
# str_mk = str(int_num_s) 
# print(f'"{int_num_s}" ({type(int_num_s)}) - {str_mk} ({type(str_mk)})') 

# print(f"1 - {bool(1)} ({type(bool(1))})") 
# print(f"0 - {bool(0)} ({type(bool(0))})") 
# print(f"100 - {bool(100)} ({type(bool(100))})") 


# # Example 5: Input and Type Conversion

# age_input = input("Enter your age: ") 
# print(f"Input type:  {type(age_input)}") 

# age = int(age_input) 
# print(f"After conversion: {type(age)}") 

# future_age = age + 5 
# print(f"After 5 years, you will be {future_age} years old") 

# Example 6: Multiple Variable Assignment

# a, b, c = 10, 20, 30 

# print(f"a = {a}, b = {b}, c = {c}") 

# total = a + b + c 
# print(f"Sum = {total}") 

# a, b = b, a 
# print(f"After swap: a = {a}, b = {b}") 

# Example 7: None Type 

# result = None 
# print(f"result = {result}") 
# print(f"Type: {type(result)}") 

# result = 100 
# print(f"result = {result}") 
# print(f"Is None ? {result is None}") 

# Example 8: Type Checking with isinstance()

# x = 10
# y = 3.14
# z = "Hello"
# flag = True
# items = [1, 2, 3]

# print(f"x is int or float ? {isinstance(x, (float, int))}") 
# print(f"z is int or float ? {isinstance(y, (float, int))}") 
# print(f"z is int or float ? {isinstance(z, (float, int))}") 
# print(f"flag is int or float ? {isinstance(flag, (float, int))}") 
# print(f"items is int or float ? {isinstance(items, (float, int))}")
# 
# 
#  
# Example 9: Variable Naming Rules

# Valid variable names
# my_name = "Rahim"        # letters and underscore
# myName = "Karim"          # camelCase
# _name = "John"            # can start with underscore
# name123 = "Doe"           # can have numbers (not at start)
# MY_CONSTANT = 100         # UPPERCASE for constants

# Invalid variable names (these will cause errors)
# 2name = "Test"          # ❌ Can't start with number
# my-name = "Test"        # ❌ Hyphen not allowed
# my name = "Test"        # ❌ Space not allowed
# class = "Test"          # ❌ 'class' is reserved keyword
# if = 10                 # ❌ 'if' is reserved keyword

# print("Valid names are working fine!")
# print(f"my_name: {my_name}")
# print(f"myName: {myName}")
# print(f"_name: {_name}")
# print(f"name123: {name123}")
# print(f"MY_CONSTANT: {MY_CONSTANT}") 

# Example 10: Memory Address with id() 

# a =100 
# b = 100 

# print(f"a = {a}, id(a) = {id(a)}")
# print(f"b = {b}, id(b) = {id(b)}") 

# print(f"a is b? {a is b}")

# a = 200 
# print(f"\nAfter changing a:") 
# print(f"a = {a}, id(a) = {id(a)}")
# print(f"b = {b}, id(b) = {id(b)}") 

# print(f"a is b? {a is b}")

# x = "Hello" 
# y = "Hello"
# print(f"\nx = {x}, id(x) = {id(x)}") 
# print(f"y = {y}, id(y) = {id(y)}") 
# print(f"x is y? {x is y}") 

# Practice Challenges 
# 1
# name = "Nirjus"
# age = 23 
# city = "Mymensingh"
# fav_colour = "Black" 

# print("Name: ", name)
# print("Age: ", age) 
# print("City: ", city) 
# print("Favorite colour: ", fav_colour) 


# # 2 
# a = 3.14159

# print("Integer :", int(a)) 
# print("String :", str(a)) 
# print("Boolean :", bool(a)) 
# print(f"Float: {float(a):.2f}")

# 3

# a = int(input("Enter a number: ")) 
# b = int(input("Enter another number: ")) 

# total = a + b 
# print("Total of your numbers: ", total) 

# 4 

# a = "Hello" 
# b = 3 
# c = 3.13 
# d = (1, 2, 3) 
# e= {1, 2, 3} 
# f = True 
# g = {"apple": "200"} 

# print(type(g), type(a), type(d), type(f), type(e), type(d), type(c))  

# Ex - 4 
a = int(input("E")) 