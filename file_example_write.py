# let's create a journal
with open("journal.txt", "a") as journal:
    while True: # infinite loop until q is pressed
        text = input("Enter a journal entry: (press q to quit):")
        if text == "q":
            break
        journal.write(text+"\n") # need to add to the new line
