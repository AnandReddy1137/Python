for letter in '!Python _is_ Awesome!':

    # break the loop as soon it sees 'e'
    # or 's'
    if letter == '_':
        continue
    print(letter)
print('Current Letter breaking the loop :', letter)

print('''
    continue: continues the loop, skipping the current iteration 
      ''')