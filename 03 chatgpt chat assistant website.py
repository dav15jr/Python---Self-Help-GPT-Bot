import openai                                                       #import the open api package
import gradio                                                       #import the gradio api package

def open_file(filepath):                                            #define what "open_file" is and does 
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()


openai.api_key = open_file('openaiapikey.txt')                      # open the file with my api key

#----------------------------Setup Above--------------------------------------------

messages = [{"role": "system", "content": "You are a self improvement coach that helps people achieve their goals"}]     # Create a list called messages, and define the role of chat gpt.

def CustomChatGPT(user_input):                                         # define a function called "CustomChatGPT" that takes one argument (text message or query), user_input,to be sent to the chatbot.
    messages.append({"role": "user", "content": user_input})           # This line appends a dictionary to a list called messages. This dictionary represents the user's message and has two key-value pairs: "role" (set to "user") and "content" (set to the user_input argument). This is how the user's message is added to the chat history.
    response = openai.ChatCompletion.create(                           # This line sends a request to OpenAI's GPT-3.5 Turbo model to generate a response. It uses the openai.ChatCompletion.create method to create a chat-based completion. 
        model = "gpt-3.5-turbo",                                       # The model parameter specifies the model to use, which is "gpt-3.5-turbo" in this case.
        messages = messages                                            # The messages parameter is set to the list of messages built up so far, including the user's input. 
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]       # This line extracts the generated response from the OpenAI API's response. It accesses the content of the assistant's reply and stores it in the variable ChatGPT_reply.
    messages.append({"role": "assistant", "content": ChatGPT_reply})   # After receiving the response from the chatbot, this line appends another dictionary to the messages list. This dictionary represents the assistant's reply and has the same structure as the user's message dictionary, with "role" set to "assistant" and "content" containing the chatbot's response..
    return ChatGPT_reply                                               # This line returns the chatbot's response to the user.

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Self Improvement Coach")

demo.launch(share=True)