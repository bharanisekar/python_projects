#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# f = open("/Users/Bharanikumar/PycharmProjects/Mail Merge Project Start/Input/Names/invited_names.txt", "r")
# print(f.readline())
with open("/Users/Bharanikumar/PycharmProjects/Mail Merge Project Start/Input/Names/invited_names.txt") as file:
    names = file.readlines()

with open("/Users/Bharanikumar/PycharmProjects/Mail Merge Project Start/Input/Letters/starting_letter.txt") as file:
    content = file.read()

for i in names:
    stripped = i.strip()
    replaced = content.replace("[name]",f"{stripped}")
    with open(f"/Users/Bharanikumar/PycharmProjects/Mail Merge Project Start/Output/ReadyToSend/letter_to_{stripped}.txt", mode = "a") as file:
        file.write(f"{replaced}")

