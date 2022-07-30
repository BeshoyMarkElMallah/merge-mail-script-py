PLACEHOLDER = "[name]"


with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents= letter_file.read()
    for name in names:
        newName=name.strip()
        new_letter=letter_contents.replace(PLACEHOLDER,newName)
        with open(f"./Output/ReadyToSend/send_to_{newName}.txt",mode="w") as ready_letter:
            ready_letter.write(new_letter)



