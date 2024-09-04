
#Write a program that uses a while loop to print out all numbers divisible by three
# in the range of 1-1000.
number = 1
while number <= 1000:
    if number % 3 == 0:
        print(number)
    number += 1

#Write a program that converts inches to centimeters until the user inputs a negative value.
#Then the program ends.
while True:
    inches = float(input("Enter inches(negative value to exit) : "))
    centimeters = inches * 2.54
    if inches < 0:
        print("Negative value entered")
        break
    print(f"{inches} inches = {centimeters} centimeters")
print("Program Terminated")

#Write a program that asks the user to enter numbers until they enter an empty string to quit.
#Finally, the program prints out the smallest and largest number from the numbers it received.
numbers = []
while True:
    number = (input("Enter a number or quit by pressing enter: "))
    if number == "":
        break
    number = int(number)
    numbers.append(number)
if numbers:
        lowest = min(numbers)
        highest = max(numbers)
        print(f"{lowest} is the lowest number and {highest} is the highest number")
else:
    print("No numbers entered")

#Write a game where the computer draws a random integer between 1 and 10.
# The user tries to guess the number until they guess the right number.
# After each guess the program prints out a text: Too high, Too low or Correct.
#Notice that the computer must not change the number between guesses.
import random
target_number = random.randint(1,10)
while True:
    user_guess = int(input("Guess a number between 1 and 10:" ))
    if user_guess == target_number:
        print("Your guess is correct!")
        break
    elif user_guess < target_number:
        print("Your guess is too low")
    elif user_guess > target_number:
        print("Your guess is too high")

#Write a program that asks the user for a username and password.
# If either or both are incorrect, the program ask the user to enter the username and password
# again.This continues until the login information is correct or wrong credentials have been
# entered five times. If the information is correct, the program prints out Welcome.
# After five failed attempts the program prints out Access denied.
# The correct username is python and password rules.
Username = "python"
Password = "rules"
attempts = 0
while attempts < 5:
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username == Username and password == Password:
        print("Welcome!")
        break
    attempts += 1
    if attempts == 5:
        print("Access denied!")
    else:
        print("Enter the username and password again")


#Implement an algorithm for calculating an approximation for the value of pi (π).
#Let's assume that A is a unit circle. A unit circle has the radius of one, and it is centered
#at the origin (0,0). Smallest possible square B is drawn around the unit circle so that
# circle A is completely inside the square. The corners of the square are now (-1,-1), (1, -1),
#(1, 1), and (-1, 1). If a large number of random points are scattered inside the square, the
# fraction of points that fall inside the circle A correlates with the fraction of the area of
# circle A compared to the area of square B: πr^2/4 = π*1^2/4 = π/4. This can be used as a
# simple method for calculating an approximation of the value of pi: Let's generate a large
# number of random points, such as one million, inside square B. Let N be the total number of
# random points. Each point inside the square is tested for whether it resides inside circle A.
# Let n be the total number of points that fall inside circle A. Now we have n/N≈π/4, and from
# that we get π≈4n/N. Write a program that asks the user how many random points to generate,
# and then calculates the approximate value of pi using the method explained above.
# At the end, the program prints out the approximation of pi to the user.
# (Notice that it is easy to test if a point falls inside circle A by testing if it fulfills
# the equation x^2+y^2<1.).
import random
num_points = int(input("How many numbers do you want to generate? "))
points_inside_circle = 0
points = 0
for points in range(num_points):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x**2 + y**2 <= 1:
        points_inside_circle += 1
pi_approximation = 4 * points_inside_circle/num_points
print(f"Approximation of π {num_points} points: {pi_approximation}")








