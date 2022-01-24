import random

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

myWord = getWord(0)
print(myWord)