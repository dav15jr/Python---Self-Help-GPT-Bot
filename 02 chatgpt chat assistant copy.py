import openai                                                       # import the open api package

def open_file(filepath):                                            # define what "open_file" is and does 
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()


openai.api_key = open_file('openaiapikey.txt')                      # open the file with my api key

messages = []                                                               # Create a list called messages
system_msg = input("What type of chatbot would you like to create?\n")      # create a variable called "system_msg" that takes an input
messages.append({"role": "system", "content": system_msg})                  # take user input and append it to the messages list

print("Your new assistant is ready!")                                       # prints out the message
while input != "quit()":                                                    # run while loop until "quit()" is entered
    message = input()                                                       # take new input for users message
    messages.append({"role": "user", "content": message})                   # take user input and append it to the messages list
    response = openai.ChatCompletion.create(                                # communicate with openai gpt-3.5-turbo api and send it messages list previously aquired
        model="gpt-3.5-turbo",
        messages=messages)
    reply = response["choices"][0]["message"]["content"]                    # create a variable called "reply" that saves the response from openai gpt-3.5-turbo
    messages.append({"role": "assistant", "content": reply})                # take reply input and append it to the messages list
    print("\n" + reply + "\n")                                              # print out the response from openai gpt-3.5-turbo, then while loop repeats.