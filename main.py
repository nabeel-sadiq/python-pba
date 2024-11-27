# Take user input as height and convert it to integer because its a string by default.
diamond_height_input = int(input("Enter height of 💎:\n"))

# Actual Diamond height is 1/2 of the user input because we are running two loops, 1 for the top part and second for the bottom part. We also have to convert it to an integer because if the user enters height 7, then 7/2 is 4.5 and you cannot run a loop 4.5 times.. so int(4.5) = 4.
diamond_height = int(diamond_height_input / 2)

# Creating a function that makes the diamond for us
def create_hollow_diamond():

  # Declaring a middle space variable with an initial value of 0.
  middle_space = 0

  # Creating a loop that decrements the value of i from the diamond height to 0.
  for i in range(diamond_height, 0, -1):

    # Here we are printing spaces before the 1st star to make it centered [(" " * i ) + "*"].
    # Then we are printing spaces in the middle of the two stars [(" " * middle_space)], the middle spaces keep increasing as we have [middle_space += 2].
    # So basically in the top part of the diamond we are printing spaces before the first star that keep decreasing, and printing spaces between the middle of the star that keep increasing.
    print((" " * i ) + "*" + (" " * middle_space) + "*")
    middle_space += 2

    # Here we have a loop to print the bottom part of the screen.
    # so in the first line we are printing spaces before the first star to keep it centered.. since the spaces before the first star (of the bottom part) needs no space, thus the loop starts off at 0.
    # The spaces before the first star keep increasing, [(" " * j ) + "*"],
    # and the spaces in middle of both stars [(" " * middle_space) + "*")], keep decreasing due to [middle_space -= 2]
  for j in range(0, diamond_height + 1, 1):
    print((" " * j ) + "*" + (" " * middle_space) + "*")
    middle_space -= 2


#calling the function here
create_hollow_diamond()

# i thought of this code myself btw and didnt take any help from gpt or the book u just need to draw some steps on a paper and understand each step of what to do one by one.