
# squares = { x: x**2 for x in range (1,6)} 
# print(squares) 

# # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25} 

# d1 = {"a": 1} 
# d2 = {"b": 2} 
# merged = d1 | d2 
# print(merged)  

# word = [ "apple", "banana", "cherry", "apple", "banana", "cherry", "apple", "banana", "cherry", "apple", "banana", "cherry"]
# c = Counter(word)
# print(c) 
# print(c.most_common(1)) 

day = input("Enter a day: ").capitalize()
match day: 
    case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
        print("It's a weekday.")
    case "Saturday" | "Sunday":
        print("It's a weekend.") 
    case _:
        print("Invalid day.") 