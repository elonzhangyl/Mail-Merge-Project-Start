#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("input/names/invited_names.txt") as file:
    names = file.read().splitlines()

for name in names:
    with open(f"output/ReadyToSend/{name}.txt", "w") as file_email:
        with open("input/letters/starting_letter.txt") as file:
            lines = file.read()
            new_lines = lines.replace("[name]", f"{name}")
        file_email.write(new_lines)