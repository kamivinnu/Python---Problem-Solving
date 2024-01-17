# exercise NUMBER GUESSING GAME
# Make a variable, like winning_number and assign any number to it.
# Ask user to guess a number.
# if user guess correctly then, print "you win !!!"
# if user didn't guess correctly then:
  # if user guessed lower than actual number then print "too low"
  # if user guessed higher than actual number then print "too high"

#google "how to generate random number in python" to generate random
# winning_number
# Solution
winning_number = 25
user_input = input("guess a number between 1 to 100 : ")
user_input = int(user_input)
if user_input == winning_number:
    print("you win !!!")

else:

     if user_input < winning_number: 
        print("too low")
    
     else:
        print("too high")
    
    # if user_input > winning_number:
    #     print("too high")
