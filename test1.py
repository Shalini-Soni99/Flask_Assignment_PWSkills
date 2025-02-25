
name = input("What is your name?").strip().title()

#Split first name and right name
first, last = name.split(" ")
print(f"Hello, {name}")