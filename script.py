import time
import random

def new_game():
     global roll_again
     print "Please input 'y' or 'n'."
     roll_again = raw_input("Roll the dices again? ")
     if (roll_again == "y"):
          print ""
     elif (roll_again == "n"):
          print "End of the game."
     else:
          new_game()

min        = 1
max        = 6
roll_again = "y"
timeout    = time.time() + 4

print "Loading the game... Please wait."
while True:
     if time.time() > timeout:
          break
     for i in ["/", "-", "|", "\\", "-", "|"]:
          print "%s\r" % i,

while (roll_again == "y"):
     print "Rolling the dices..."
     time.sleep(4)
     print "The values are:"
     first_number = random.randint(min, max)
     print first_number
     second_number = random.randint(min, max)
     print second_number
     if (first_number == 6 and second_number == 6):
          print "You win!"
     roll_again = raw_input("Roll the dices again? ")
     if (roll_again == "y"):
          continue
     elif (roll_again == "n"):
          print "End of the game."
     else:
          new_game()
