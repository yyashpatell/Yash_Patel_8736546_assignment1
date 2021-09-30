print("------------------WELCOME TO OUR SHOP--------------------")

shirt_price = 9.99

shirt_color = input("\nEnter the color of shirt: ")

option = int(input("\nDo you want Polo-Shirt or T-shirt(For Polo-Shirt enter 1 and for T-Shirt enter 2: "))

if option == 1:

  shirt_type = "Polo-Shirt"
  print("\nThe type of shirt you select is", shirt_type)

elif option == 2:

  shirt_type = "T-Shirt"
  print("\nThe type of shirt you select is ", shirt_type)
else:

  print("Incorrect number")

num_shirt = int(input("\nNumber of shirts: "))

total = shirt_price*num_shirt

tax = 0.13 * total

final_total = tax+total

print("\nThe color of your shirts are: ",shirt_color)

print("\nThe total number of shirt yor want are: ",num_shirt)

print("\nYour price before adding HST is",total)

print("\nYour total price after adding HST is",final_total)