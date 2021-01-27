#Round1Math Game: asks a series of simple maths questions and scores answers, layers of complexity include speed, operator difficulty, memory element

import random
import operator
import time
import replit
import threading

#Beginning - Greeting
name = input("What is your name? ")
time.sleep(1)

#Instructions
print(f" \n{name}, beat the timer and answer atleast 5 questions correctly")
print('\nL E V E L 1!!! ')
time.sleep(2)
print("Good Luck, I hope you know your math well", name, "!")

loss = 0
score = 0
time.sleep(2)
print(f"Your score is {score}!")

#Dictionary of operators
operators = { 
  '+': operator.add, 
  '-': operator.sub,
  'x': operator.mul,
  #'/': operator.truediv,
}
#function that generates a random maths question and then checks to see whether user answer is equal to true answer
def random_question():
  num_1 = random.randint(1,10)
  num_2 = random.randint(1,10)

  operation = random.choice(list(operators.keys()))
  print('\nWhat is '+ str(num_1) + operation + str(num_2) +'?')
  player_answer = input()
  answer = operators[operation](num_1,num_2)

  if float(player_answer) == answer:
    print('Correct!')
    global score
    score += 1    
  else:
    print('Incorrect!')
    global loss
    loss +=1
  
  print(f" Your score is {score}!")

input('\nPress enter to continue')
#10 second timer 
def timer(): 
    global my_timer
    my_timer = 10
    for x in range(10):
      my_timer = my_timer - 1
      time.sleep(1)
    print('Out of Time!')
    
#allows two functions to run concurrently (random_question&timer)
countdown_thread = threading.Thread(target = timer)
countdown_thread.start()

#ask random question as long as timer is non zero, win-lose scenario
while my_timer > 0:
  random_question()
  print(f"{my_timer} seconds left!")
  if score > 4 and my_timer == 0:
    time.sleep(2)
    print("YOU WON! But wait...")
    time.sleep(1.5)
    print(f"So you know your math, lets hope you know your capitals. Time for the next game!")
    time.sleep(5)
    input('\nPress enter to continue')
    replit.clear()
if score < 5:
    print('You loser!!!')
    quit()

# *************Game 2 : Remember the Colours*************

#Players have to remember the random colour sequence and input answers when prompted, three rounds; round one- 3 colours, round two- 7 colours, round three- 12 colours
print('\nL E V E L 2!!! ')
print(f" \n{name},your task is to try & remember the colours in order")

score = 0
loss = 0
time.sleep(2)

print(f"\nYour score is {score}, win all 3 rounds to win the game ")

time.sleep(2)

print("\nI hope you've got a good memory " + name + "!")
input('\nPress enter to continue')


#Timer
def countdown(t):

    while t:
        mins, secs = divmod(t, 5)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    print('Lets go!!')


# 3 second countdown
countdown(int(3))


#Flashes a list of colours in terminal one by one
def overprint(colour_list, t=1, char=" "):
    for i in range(len(colour_list)):
        time.sleep(t)
        print(
            '\r{0:{1}<{2}}'.format(colour_list[i], char,
                                   len(colour_list[i - 1])),
            end="\r")
    time.sleep(t)
    print('\r{0:{1}<{2}}'.format(" ", char, len(colour_list[-1])), end="\r")


Colours = [
    'red', 'blue', 'green', 'purple', 'yellow', 'orange', 'black', 'white',
    'pink'
]
#Generate a random list of n colours from list Colours and feed into overprint. Checks to see if user recalls colours correctly for 3 rounds of increasing difficulty.
for i in range(1, 4):
    time.sleep(1)
    print('\n' 'Round', i)
    colours_shown_to_player = random.sample(Colours, 2 * i + 1)
    overprint(colours_shown_to_player)

    print('\nWhat colours were just shown to you?')
    user_answer = input()

    if user_answer.replace(',', ' ').lower().split(
    ) == colours_shown_to_player:  #' '.join(round_answer):
        print('Correct!')
        score += 1
    else:
        print('Incorrect!')
        loss += 1

    print(f"Your score is {score}")

#User can only win game if they win all 3 rounds
if loss > 0:
    print('YOU LOSE! Try Again')
    input('\nPress enter to continue')
    replit.clear()

else:
    print('YOU WIN!! Please speak to Muhammed to claim your £1000 amazon voucher!')
    input('\nPress enter to continue')
    replit.clear()


# *************Game 3 : Guess the Capitals*************

#Greeting
print(f"\nL E V E L 3!!! I hope you know your capitals well {name}!")
print(f" \nAnswer 5 questions {name} to win this game!")

score = 0
print(f"Oh also, your score is {score} " + name)
input('\nPress enter to continue')

loss = 0

#Dictionary with Countries & Cities
Countries = {
    'England': 'London',
    'Spain': 'Madrid',
    'Japan': 'Tokyo',
    'China': 'Beijing',
    'India': 'New Delhi',
    'Nigeria': 'Abuja',
    'Ireland': 'Dublin',
    'Australia': 'Canberra',
    'Turkey': 'Ankara',
    'Sweden': 'Stockholm',
    'Italy': 'Rome',
    'Russia': 'Moscow',
    'Egypt': 'Cairo',
    'Syria': 'Yemen',
    'South Africa': 'Johannesburg',
    'Gambia': 'Banjul',
    'Brazil': 'Rio',
    'Chile': 'Santiago',
    'Canada': 'Ottawa',
    'USA': 'Washington DC',
    'Ghana': 'Accra',
    'Rwanda': 'Kigali',
    'Cameroon': 'Yaounde',
    'Norway': 'Oslo',
    'UAE': 'Abu Dhabi',
    'Germany': 'Berlin',
    'Israel': 'Tel Aviv'
}


# Function will choose one random word from this list of countries
def capital_question():
    time.sleep(1)
    Random_Country = random.choice(list(Countries.keys()))
    print(f"\nGuess the capital of {Random_Country}!")
    user_answer = input()

    if str(user_answer) == Countries[Random_Country]:
        print('Correct!')
        global score
        score += 1
    else:
        print('Incorrect!')
        global loss
        loss += 1
    print(f"Your score is {score}, you have {3 - loss} chance(s) left")


#Loop the whole game
for i in range(10):
    capital_question()
    if score > 4:
        replit.clear()
        break
        print('YOU WIN!')
        input('\nPress enter to continue')
        replit.clear()
    if loss > 2:
        print('YOU LOSE')
        input('\nPress enter to continue')
        replit.clear()
        break

#Bonus Game - Rock Paper Scissors

#Rock Paper Scissors

#Greet the player and ask for their name.
#The player must input rock paper or scissors
#Make game randomly show rock paper or scissors

#Options

#Rock
#If player puts rock and computer puts scissors player wins computer loses a point
#If player puts rock and computer puts paper player loses a point and computer wins
#If player puts rock and computer puts rock call a tie for that round

#Scissors
# If player puts scissors and computer puts rock player loses
# If player puts scissors and computer puts paper player wins and computer loses
# If player puts scissors and computer puts scissors call tie

#Paper
#If player puts paper and computer puts rock player wins round and computer loses
# If player puts paper and computer puts scissors player loses and computer wins
# If player puts paper and computer puts paper call tie

#Once players score is >4 then player wins
#Once players loss is >2 then player loses.
#Loop the game again for 5 times!

score = 0
loss = 0
