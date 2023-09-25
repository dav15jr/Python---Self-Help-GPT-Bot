import openai                                                       #import the open api package
import gradio                                                       #import the gradio api package

def open_file(filepath):                                            #define what "open_file" is and does 
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()


openai.api_key = open_file('openaiapikey.txt')                      # open the file with my api key, which is used to connect my open ai account

#----------------------------Setup Above--------------------------------------------

messages = [{"role": "system", "content": "You are a helpful self-improvement coach, who gives practical guidance and tips based on proven methods \
from experts in the field. Answer in a simple instructional way that is easy for the user to understand and implement in their lives.\
You suggest different techniques, methods, books etc to help the user achieve their goal or overcome their challenges."}]\

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages,
        temperature = 1,
        max_tokens = 213,
        top_p = 1,
        frequency_penalty = 0,
        presence_penalty = 0
    )
    
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})


    return ChatGPT_reply

#----------------------------Output Setup Below--------------------------------------------

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Your AI Self Help Coach")

demo.launch(share=True)
