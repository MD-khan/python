def pig_latin(text):
  say = ""
  # Separate the text into words
  words = text.split()
  for word in words:
    # Create the pig latin word and add it to the list
    say += " " + word[1:] + word[:1] + "ay"
    # Turn the list back into a phrase
  return say
  
  print(pig_latin("hello how are you doing")) # Should be "ellohay owhay reaay ouyay"
