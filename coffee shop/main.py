from formatting import to_title_case

print("Welcome to Erik's Coffee Shop!")

name = input("Please enter your name: ")
print(f"Welcome, {to_title_case(name)}!")

drink = input("Please enter your drink: ")
print(f"You've chosen {to_title_case(drink)} drink.")

flavor = input("Please enter your flavor: ")
print(f"You've chosen {to_title_case(flavor)} flavor.")

topping = input("Please enter your topping: ")
print(f"You've chosen {to_title_case(topping)} topping.")

print("Here's your order details: \n")
