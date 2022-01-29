import random
from colorama import init
from termcolor import colored

def getWord(num):
  with open("words", 'r') as fp:
      # To store lines
      lines = ""
      for i, line in enumerate(fp):
          # read line 4 and 7
          if i == num:
              lines += line.strip()
              break
  return lines


init() #initialise colorama "colored" method

com_word = getWord(random.randint(0,49)).upper()
#print(com_word) 

solved = False #To flag if puzzle is solved
max_tries = 6 #number of trials allowed
tries = 1 #starting trial number
guess_history = [] #collects all guesses to display for user

#main guess loop: loop while it isn't solved and there are still trials remaining
while not solved and tries <= max_tries:
  #Ask player for a 5-letter word
  print("Try "+ str(tries))
  player_word = list(input("Please enter 5-letter word: ")[0:5].upper())

   #check if words are the same
  if player_word == com_word:
      solved = True
  #create a temporary com_word (to delete used letters)
  temp_com_word = list(com_word)
  #assume all incorrect first
  solution = []
  for letter in player_word:
    solution.append(colored(letter,"white","on_grey"))
  #look for complete matches first
  for i in range(0,len(player_word)):
    if player_word[i] == temp_com_word[i]:
      solution[i] = colored(player_word[i],"white","on_green")
      player_word[i] = "#"
      temp_com_word[i] = "-"
  #check for matches but not in right place
  for i in range(0,len(player_word)):
    for j in range(0,len(temp_com_word)):
      if player_word[i] == temp_com_word[j]:    
        solution[i] = colored(player_word[i],"white","on_yellow")
        player_word[i] = "#"
        temp_com_word[j] = "-"
        break
  #Add guess to history and print alls guesses
  this_history = ""
  for k in solution:
    this_history += k
  guess_history.append(this_history)
  for h in guess_history:
    print(h)
  print("")
  #increment tries count
  tries += 1 

#if it was successfully solved, congratulate, else tell answer.
if solved:
  print("You did it in ", tries-1, " tries!")
else:
  print("Hard luck, the word was: ", com_word)
