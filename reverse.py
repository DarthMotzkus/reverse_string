#input of the string to reverse it

text = input("Write any word: ")

if text:
  print (f'Your word is: {text}')
  print (f'Your Reversed word is: {text[::-1]}')
else:
  print("You did not write a word")

#end of the program
