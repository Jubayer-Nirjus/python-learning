
with open("sample.txt","w") as f:
    f.write("Hello Python")

with open("sample.txt","r") as f:
    print(f.read()) 

# Multiplication table
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i*j}")
    print("-" * 10) 