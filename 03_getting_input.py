# Ask the user for their name
username = input("What is your name? ")

# Ask the user for their favourite integer
fav_num = int(input("Favourite Number? "))

# Double, halve the square number
doubled = fav_num * 2
halfed = fav_num / 2
squared = fav_num * fav_num

print()
# Greet the user
print("Hi {}, your favourite number is {}".format(username, fav_num))
print()
# Output the results of doubling, halving and squaring favourite number
print("Double of {} is {}".format(fav_num, doubled))
print("Half of {} is {}".format(fav_num, halfed))
print("{} squared is {}".format(fav_num, squared))

print()