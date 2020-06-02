import random 

guess = int(input("Guess my number: "))

random_number = random.randint(1, 10)

end_message = "the number was " + str(random_number)

if guess == random_number:
    print("You guessed correctly")
else:
    print(end_message)
