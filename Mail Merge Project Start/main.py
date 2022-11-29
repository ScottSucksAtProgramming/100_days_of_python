#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


# save the text file of names as a list called invites.
invites = open("Input/Names/invited_names.txt")
# save the letter text as variable called letter.
letter = open("Input/Letters/starting_letter.txt").read()

# go through each name in the lists invites.
for name in invites:
    invitee = name.strip("\n") # strip off the characters that cause the new line. save as invitee
    new_letter = letter.replace("[name]", invitee)  # replace the [name] placeholder with the name after it's stripped
    n_letter = open(f"./Output/ReadyToSend/{name}.txt", "w") # Open / Create a file called the name we're looking at.
    n_letter.write(new_letter) # Write the new letter with the name included into that file.
    print(n_letter)

invites.close()
n_letter.close()

