#false condition
x = 5

if x > 9:
    print("Hello, World!")
print('--------------------------------')
x = 10
if x > 9:
    print("Hello, World!")

print('-------------------------------')

#true condition
color = "Blue"

if color == "Blue":
    print("This is my favorite color")

print('-------------------------------')
x = 15

if x > 9:
    print("Hello!")

print("End")

print('-------------------------------')
favorite_season = "Summer"

if favorite_season == "Summer":
    print("That is my favorite season too!")

print('-------------------------------')

#if else condition
x = 15

if x > 9:
    print("Hello!")
else:
    print("Bye!")

print("End")

print('-------------------------------')

x = 5

if x > 9:
    print("Hello!")
else:
    print("Bye!")

print("End")

print('-------------------------------')
#if elif else is true
x = 5

if x < 9:
    print("Hello!")
elif x < 15:
    print("It's great to see you")
else:
    print("Bye!")

print("End")

print('-------------------------------')

#condition false
x = 25

if x < 9:
    print("Hello!")
elif x < 15:
    print("It's great to see you")
else:
    print("Bye!")

print("End")

print('-------------------------------')

#multiple elif
if favorite_season == "Winter":
    print("That is my favorite season too")
elif favorite_season == "Summer":
    print("Summer is amazing")
elif favorite_season == "Spring":
    print("I love spring")
else:
    print("Fall is my mom's favorite season")