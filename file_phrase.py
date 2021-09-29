def check():

# open the file
    with open('file_phrase.txt') as f:
        file = f.readlines()
    
# get input from user
    text = input("Enter the text you are searching: ")

# checking if input text is in file
    for line in file:
        if text in line:
            return True
    return False


# returns
if check():
    print('True')
else:
    print('False')