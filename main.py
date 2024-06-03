import random

name = input("Hello user, what is your name? ") #ask the user for their name and welcome them
print(
    f"\nWelcome {name}. I have thought of a number in the range 1-10. Now, you make have to guess.\n"
)

comp_number = random.randint(1, 10) #Computer selects the number in the range 1-10
player_lives = 5 #Initialize player lives 
tries = 0 #Initialize the number of tries by the user

while player_lives >= 0: 
  if (player_lives == 0):
    print("You are out of lives. Better luck next time \n") #If the player has used all his lives, print this 
    break
    
  else:
    try:
      user_input = int(input("Make a guess \n")) #Otherwise ask the user for an integer input
      tries += 1
      
    except Exception:
      print("Please enter an int \n") #If the user does not enter an int, throw an exception and ask him to enter an int
      continue

    choice = abs(comp_number - user_input) #Subtract the two numbers to get the difference 
    
    if (abs(choice) == 0): #If the difference is 0, then user guessed the correct number
      print(f"\n You guessed the number in {tries} tries. The number was {comp_number} \n")
      break

    elif (abs(choice) < 2): #If the differencs is 1, then display that he is close
      player_lives -= 1
      print("You are close \n")

    elif (abs(choice) >= 2 and abs(choice) < 5 and (user_input > comp_number)): #If the difference is between 2 and 5 and user's input is greater than computer's then the guess is high
      player_lives -= 1
      print("Your guess is high \n")

    elif (abs(choice) >= 5 and abs(choice) <= 10 and (user_input > comp_number)): #If the difference is between 5 and 10 and user's input is greater than computer's, then the guess is too high
      player_lives -= 1
      print("Your guess is too high \n")

    elif (abs(choice) < 5 and (comp_number > user_input)): #If the difference is less than 5 and computer's input is greater than user's, then the guess is low
      player_lives -= 1
      print("Your guess is low \n")

    elif (abs(choice) >= 5 and abs(choice) <= 10 and (comp_number > user_input)): #If the difference is between 5 and 10 and computer's input > user, then the guess is too low
      player_lives -= 1
      print("Your guess is too low \n")
